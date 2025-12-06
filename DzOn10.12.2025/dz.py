class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if amount>self.__balance:
            raise ValueError('На счете недостаточно средств')
        self.__balance-=amount
    def transfer(self,account,amount):
        if amount>self.__balance:
            raise ValueError('На счете недостаточно средств')
        self.__balance-=amount
        account.deposit(amount)



class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or new_name == '' or not new_name.isalpha():
            raise ValueError("Некорректное имя")
        self.__name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age < 0 or new_age > 110:
            raise ValueError("Некорректный возраст")
        self._age = new_age



class  IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            ip=ipaddress.split('.')
            if len(ip)!=4:
                raise ValueError('Должно быть 4 целых числа')
            self.ip = [int(part) for part in ip]
        elif isinstance(ipaddress, (list, tuple)):
            if len(ipaddress)!=4:
                raise ValueError('Должно быть 4 целых числа')
            self.ip = list(ipaddress)
        else: raise TypeError('Неправильный тип')

        for part in self.ip:
            if part < 0 or part > 255:
                raise ValueError('Каждое число в наборе принадлежит интервалу от 0 до 255')

    def __str__(self):
        return '.'.join(str(part) for part in self.ip)

    def __repr__(self):
        return f"IPAddress('{self}')"

ip1=IPAddress('172.16.31.10')
ip2=IPAddress([172,16,31,10])

print(ip1)
print(ip2)
print(repr(ip1))
print(repr(ip2))



class Word:
    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('Неправильный тип данных')
        if word=='':
            raise ValueError('Слово должно содержать хотя бы 1 букву')
        if not word.isalpha():
            raise ValueError('Слово должно содержать только буквы')
        self.word = word

    def __repr__(self):
        return f"Word('{self.word}')"
    def __str__(self):
        return self.word.capitalize()


    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) == len(other.word)
    def __ne__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) != len(other.word)
    def __lt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) < len(other.word)
    def __gt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) > len(other.word)
    def __le__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) <= len(other.word)
    def __ge__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) >= len(other.word)

word1=Word('HELLO')
print(word1)
print(repr(word1))



class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        if not all(isinstance(i, (int, float)) for i in [proteins, fats, carbohydrates]):
            raise TypeError('Неправильный тип данных')
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(
            self.proteins + other.proteins,
            self.fats + other.fats,
            self.carbohydrates + other.carbohydrates
        )
    def __mul__(self, n):
        if not isinstance(n, (float, int)):
            return NotImplemented
        return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if not isinstance(n, (float,int)):
            return NotImplemented
        return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)

    def __floordiv__(self, n):
        if not isinstance(n, (float,int)):
            return NotImplemented
        return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)

chocolate=FoodInfo(2, 2, 2)
print(repr(chocolate))
print(chocolate*2)