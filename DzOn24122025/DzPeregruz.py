class Negator:
    @staticmethod
    def neg(n):
        if isinstance(n,(int,float)):
            return -n
        elif isinstance(n,bool):
            return not n
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')

from datetime import date
class BirthInfo:
    def __init__(self,birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif  isinstance(birth_date,str):
            try:
                self.birth_date = date.fromisoformat(birth_date)
            except (ValueError, TypeError):
                raise TypeError('Аргумент переданного типа не поддерживается')
        elif isinstance(birth_date,(list,tuple)):
            try:
                year, month, day = birth_date
                self.birth_date = date(year, month, day)
            except (ValueError, TypeError):
                raise TypeError('Аргумент переданного типа не поддерживается')
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        year=date.today().year-self.birth_date.year
        if (date.today().month, date.today().day) < (self.birth_date.month, self.birth_date.day):
            year -= 1
        return year

birthinfo = BirthInfo(date(2023, 2, 26))
print(birthinfo.age)
