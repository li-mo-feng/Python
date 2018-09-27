class Date:

    def __init__(self,day=0, month=0, year=0):
        self.day=day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int,date_as_string.split('-'))
        my_date = cls(day, month, year)
        return my_date

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


if __name__ == '__main__':
    my_date = Date.from_string('11-09-2012')
    print(my_date.day, my_date.month,my_date.year)
    is_date = Date.is_date_valid('13-13-2012')
    print(is_date)
