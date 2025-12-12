from abc import ABC, abstractmethod

# 1 ZAD
class ChessPiece(ABC):
    def __init__(self,horizontal, vertical):
        if horizontal not in 'abcdefgh' or not 1 <= vertical <= 8:
            raise ValueError("")
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self,horizontal, vertical):
        pass

class King(ChessPiece):
    def can_move(self,horizontal, vertical):
        if horizontal not in 'abcdefgh' or not 1 <= vertical <= 8\
                or (self.horizontal == horizontal and self.vertical == vertical):
            return False
        return abs(self.vertical -vertical) in [0,1] and abs(ord(self.horizontal) -ord(horizontal)) in [0,1]

class Knight(ChessPiece):
    def can_move(self,horizontal, vertical):
        if horizontal not in 'abcdefgh' or not 1 <= vertical <= 8\
                or (self.horizontal == horizontal and self.vertical == vertical):
            return False
        vert=abs(self.vertical -vertical)
        horiz=abs(ord(self.horizontal) -ord(horizontal))
        return (vert==1 and horiz==2)or(vert==2 and horiz==1)

King1=King('a',1)
Knight1=Knight('a',1)
for hor in 'abcdefgh':
    for ver in [1,2,3,4,5,6,7,8]:
        print(f"For horizontal:{hor} vertical:{ver}")
        print(King1.can_move(hor, ver))
        print(Knight1.can_move(hor, ver))



# 2 ZAD
class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood='strict'

class Mother:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood='kind'

class Daughter(Mother,Father):
    pass

class Son(Father,Mother):
    pass

daughter1=Daughter()
print(daughter1.greet())
print(daughter1.mood)
daughter1.be_strict()
print(daughter1.mood)



# 3 ZAD
class TimeForCountry(ABC):
    def __init__(self, year, month, day):
        if not (1 <= day <= 31) or not (1 <= month <= 12) or not (1 <= year <= 9999):
            raise ValueError("")
        self.year = year
        self.month = month
        self.day = day

    @abstractmethod
    def format(self):
         pass

    def iso_format(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

class USADate(TimeForCountry):

    def format(self):
        return f"{self.month:02d}-{self.day:02d}-{self.year:04d}"

class ItalianDate(TimeForCountry):
    def format(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"

usa=USADate(2025,12,11)
italian=ItalianDate(25,2,1)
print(usa.iso_format())
print(italian.iso_format())
print(usa.format())
print(italian.format())