from mrjob.job import MRJob
import sys


class Movies(MRJob):
    def mapper(self, _, line):
        user = line.split(',')[0]
        movie = line.split(',')[1]
        rating = line.split(',')[2]
        genre = line.split(',')[3]
        date = line.split(',')[4]

        if user != "Usuario" and movie != "Movie" and rating != "Rating" and genre != "Genre" and date != "Date":
            yield f"Movies watched by {user}", int(rating)
            yield "Max and min movies", date
            yield f"Number of users watching {movie}", int(rating)
            yield "Best and worst rating days", (date, int(rating))
            yield f"Best and worst movie of genre {genre}", (movie, int(rating))

    def reducer(self, key, values):
        total = 0
        count = 0
        if key.__contains__('Movies watched'):
            for v in values:
                total += v
                count += 1

            avg = total/count
            yield key, f"Number of movies: {count}, Average rating: {avg}"

        elif key.__contains__('Max and min'):
            dates = {}
            for v in values:
                try:
                    dates[v] = dates[v] + 1
                except Exception:
                    dates[v] = 0
                    dates[v] = dates[v] + 1

            max_day = max(dates.items(), key=lambda x: (x[1]))
            yield key, f"max: date: {max_day[0]} number of movies: {max_day[1]}"
            min_day = min(dates.items(), key=lambda x: (x[1]))
            yield key, f"min: date: {min_day[0]} number of movies: {min_day[1]}"

        elif key.__contains__('Number of users'):
            for v in values:
                total += v
                count += 1

            avg = total / count

            yield key, f"users: {count}, rating: {avg}"

        elif key.__contains__('rating days'):
            dates = {}
            ratings = {}
            for v in values:
                try:
                    dates[v[0]] = dates[v[0]] + 1
                    ratings[v[0]] = ratings[v[0]] + v[1]
                except Exception:
                    dates[v[0]] = 0
                    ratings[v[0]] = 0
                    dates[v[0]] = dates[v[0]] + 1
                    ratings[v[0]] = ratings[v[0]] + v[1]

            for date in dates:
                count = dates[date]
                total_rating = ratings[date]
                dates[date] = total_rating / count

            max_day = max(dates.items(), key=lambda x: (x[1]))
            yield key, f"Best rating day: {max_day[0]} rating: {max_day[1]}"
            min_day = min(dates.items(), key=lambda x: (x[1]))
            yield key, f"Worst rating day: {min_day[0]} rating: {min_day[1]}"

        elif key.__contains__('genre'):
            movies = {}
            ratings = {}
            for v in values:
                try:
                    movies[v[0]] = movies[v[0]] + 1
                    ratings[v[0]] = ratings[v[0]] + v[1]
                except Exception:
                    movies[v[0]] = 0
                    ratings[v[0]] = 0
                    movies[v[0]] = movies[v[0]] + 1
                    ratings[v[0]] = ratings[v[0]] + v[1]

            for movie in movies:
                count = movies[movie]
                total_rating = ratings[movie]
                movies[movie] = total_rating / count

            best_movie = max(movies.items(), key=lambda x: (x[1]))
            worst_movie = min(movies.items(), key=lambda x: (x[1]))
            yield key, f"Best: {best_movie[0]} rating: {best_movie[1]}, Worst: {worst_movie[0]} rating: {worst_movie[1]}"


if __name__ == '__main__':
    Movies.run()
