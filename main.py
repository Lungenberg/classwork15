"""
# Повторение
def function():
    n = int(input("Введите число: "))
    m = n*n-2
    print(m)
function()

def function1(x):
    y = x*x-2
    print(y)
x = int(input("Введите число: "))
function1(x)

def function2():
    first_name = 'Jason'
    last_name = 'Statham'
    full_name = first_name + " " + last_name
    print(full_name)
    new = str(input("Введите новую фамилию: "))
    print(first_name + " " + new)
function2()

def function3(c, o):
    g = c + o
    k = c*2 + o*4
    print("Количество голов = ", g)
    print("Количество конечностей = ", k)
c = int(input("Введите количество кур "))
o = int(input("Введите количество овечек "))
function3(c, o)

class Name():
    name = ""
    surname = ""
    new_surname = ""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def wedding(self):
        self.new_surname = str(input("Введите новую фамилию: "))
        self.surname = self.new_surname
        print(self.surname, self.new_surname)
fish = Name('Jason', 'Statham')
fish.wedding()
print(fish.surname)

class Bird():
    def can_fly(self):
        print("This bird can fly")
    def cannot_fly(self):
        print("This bird cannot fly")

class Parrot(Bird):
    def can_fly(self):
        print("Yes, it is")
class Qiwi(Bird):
    def cannot_fly(self):
        print("Yes, it is")
aboba = Qiwi()
aboba.can_fly()
"""
# Инкапсуляция
class Dom_Animals():
    name = ""
    breed = ""
    color = ""
    age = 0

    def starenie(self):
        self.age = self.starenie + 1

    def starenie(self):
        self.age = self.age + 1

    def new_name(self):
        self.name = input("Введите новое имя: ")

class Cats(Dom_Animals):
    def starenie(self):
        self.age = 4
        self.age = self.age + 7
        print(self.age)
ob = Cats
ob.starenie()
ob.starenie()














