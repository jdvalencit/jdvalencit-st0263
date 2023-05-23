from mrjob.job import MRJob
import sys


class StockValue(MRJob):
    def mapper(self, _, line):
        company = line.split(',')[0]
        price = line.split(',')[1]
        date = line.split(',')[2]

        if company != "Company" and price != "price" and date != "date":
            yield f"Dia mayor valor: {company}", (date, float(price))
            yield f"Dia menor valor: {company}", (date, float(price))
            yield "Lista de acciones crecientes", (company, float(price))
            yield "Dia negro", (date, float(price))

    def reducer(self, key, values):
        if key.__contains__('Dia mayor'):
            max = 0
            max_date = ""
            for v in values:
                if v[1] > max:
                    max_date = v[0]
                    max = v[1]

            yield key, f"{max_date}: {max}"

        elif key.__contains__('Dia menor'):
            min = sys.maxsize
            min_date = ""
            for v in values:
                if v[1] < min:
                    min_date = v[0]
                    min = v[1]
            yield key, f"{min_date}: {min}"

        elif "Lista" in key:
            prev = 0
            up = False
            stock = ""
            for v in values:
                if v[1] >= prev:
                    up = True
                    stock = v[0]
                    prev = v[1]
            if up:
                yield key, stock

        elif key.__contains__('negro'):
            days = sorted(values, key=lambda x: (x[1]))

            yield key, days[0][0]


if __name__ == '__main__':
    StockValue.run()
