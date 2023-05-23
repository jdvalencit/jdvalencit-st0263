from mrjob.job import MRJob


class EmployeeData(MRJob):
    def mapper(self, _, line):
        employee = line.split(',')[0]
        sector = line.split(',')[1]
        salary = line.split(',')[2]

        if salary != "salary" and employee != "idemp" and sector != "sector":
            yield f"Average salary of sector {sector}:", int(salary)
            yield f"Average salart of employee {employee}:", int(salary)
            yield f"Employees of sector {sector}:", employee

    def reducer(self, key, values):
        sum = 0
        total = 0

        if key.__contains__('Employees of sector'):
            for _ in values:
                sum += 1

            yield key, sum
        else:
            for v in values:
                total += v
                sum += 1

            avg = total / sum
            yield key, avg


if __name__ == '__main__':
    EmployeeData.run()
