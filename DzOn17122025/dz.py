from itertools import product


class Counter:
    def __init__(self,start=0):
        if start<0:
            raise ValueError('Число не меньше 0')
        self.value=start

    def inc(self,n=1):
        if n<0:
            raise ValueError('Число не меньше 0')
        self.value+=n

    def dec(self,n=1):
        if n<0:
            raise ValueError('Число не меньше 0')
        self.value = max(0, self.value - n)

    def __str__(self):
        return f"{self.value}"

class NonDecCounter(Counter):
    def dec(self,n=1):
        ...

class LimitedCounter(Counter):
    def __init__(self,start=0,limit=10):
        if start>limit:
            raise ValueError('Лимит не меньше старта')
        super().__init__(start)
        self.limit=limit

    def inc(self,n=1):
        if n<0:
            raise ValueError('Число не меньше 0')
        self.value = min(self.value + n, self.limit)

one=Counter(1)
two=NonDecCounter(100)
three=LimitedCounter()
#print(one.inc(-1))
one.dec(10)
print(one)
two.dec(10)
print(two)
three.inc(20)
print(three)



class Bachelor:
    def __init__(self, firstName,lastName,group,averageMark):
        if not all(isinstance(i, str) for i in (firstName, lastName, group)) or not isinstance(averageMark,(int,float)):
            raise ValueError('Неправильные данные')
        self.firstName=firstName
        self.lastName=lastName
        self.group=group
        self.averageMark=averageMark

    def getScholarship(self):
            return 10000 if self.averageMark==5 else 5000 if self.averageMark>3 else 0

class Undergraduate(Bachelor):
    def __init__(self, firstName, lastName, group, averageMark, research_topic=None):
        super().__init__(firstName, lastName, group, averageMark)
        self.research_topic = research_topic

    def getScholarship(self):
            return 15000 if self.averageMark==5 else 7500 if self.averageMark>3 else 0

print([i.getScholarship() for i in [Bachelor("Bob","Bobikov","14121",5),
                                    Bachelor("Nikita","Nikitovich","14121",4),
                                    Bachelor("Sharik","Sharikov","14121",2),
                                    Undergraduate("Bob", "Bobikov", "14127", 5),
                                    Undergraduate("Nikita", "Nikitovich", "14127", 4),
                                    Undergraduate("Sharik", "Sharikov", "14127", 2)]])



class Product:
    def __init__(self,name,cost,weight):
        self.__name=name
        self.__cost=cost
        self.__weight=weight

    def get_cost(self):return self.__cost

    def get_weight(self):return self.__weight

    def get_name(self):return self.__name

    def set_name(self, name): self.__name = name

    def set_cost(self, cost): self.__cost = cost

    def set_weight(self, weight): self.__weight = weight

class Buy(Product):
    def __init__(self,name,cost,weight,count):
        super().__init__(name,cost,weight)
        self.__count=count

    def get_count(self):return self.__count

    def set_count(self, count): self.__count = count

    def get_costAll(self):
        return self.__count*self.get_cost()

    def get_weightAll(self):
        return self.__count*self.get_weight()

class Check(Buy):
    def show(self):
        return (f"Имя товара: {self.get_name()}\n"
                f"Кол-во товаров: {self.get_count()}\n"
                f"Вес товаров: {self.get_weightAll()}\n"
                f"Цена товаров: {self.get_costAll()}")

toBuy=Check('Яблоко',10,100,500)
print(toBuy.show())



import math
class Figure():
    def volume(self):
        raise NotImplemented

    def area(self):
        raise NotImplemented

    def __str__(self):
        return f"{self.__class__.__name__}: объём-{self.volume()}, площадь поверхости-{self.area()}"

class Parallelepiped(Figure):
    def __init__(self,length,width, height):
        self.length=length
        self.width=width
        self.height=height

    def volume(self):
        return self.length*self.width*self.height

    def area(self):
        return 2*(self.length*self.width + self.length*self.height + self.width*self.height)

class Cube(Parallelepiped):
    def __init__(self,length):
        super().__init__(length,length,length)

class Ellipsoid(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return (4 / 3) * math.pi * self.a * self.b * self.c

    def area(self):
        p = 1.6075
        return 4 * math.pi * (
                    ((self.a ** p * self.b ** p + self.a ** p * self.c ** p
                      + self.b ** p * self.c ** p) / 3) ** (1 / p))

class Sphere(Ellipsoid):
    def __init__(self,radius):
        super().__init__(radius,radius,radius)
        self.radius=radius

    def area(self):
        return 4*math.pi*(self.radius**2)

class Cylinder(Figure):
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height

    def volume(self):
        return math.pi* (self.radius**2)*self.height

    def area(self):
        return 2*math.pi*self.radius*self.height+2*math.pi*(self.radius**2)

def checkVolume(figures):
    if not figures:
        return 'Список пуст'
    sumVolumes=sum(i.volume() for i in figures)
    volumes=[i for i in figures if i.volume()>=sumVolumes-i.volume()]
    return volumes if volumes else 'Нет таких фигур'

figures = [
        Cube(25),
        Sphere(3),
        Cylinder(2, 5),
        Parallelepiped(3, 4, 5),
        Ellipsoid(2, 3, 4)
    ]

result = checkVolume(figures)
if isinstance(result, str):
    print(result)
else:
    print(*result)


