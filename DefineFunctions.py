def HelloWorld():
    print("Hello World")

def NumbersNow():
    print("Your Numbers Are")

def NumbersLater():
    print("Your Numbers Will Be")

def PrintEachLoopItem():
    NumberLoop = [2, 4, 6, 8]
    for x in NumberLoop:
            print(x)

def PrintEachLoopItemDoubled():
    DoubledNumberLoop = [2, 4, 6, 8]
    for x in DoubledNumberLoop:
        print(x * 2)

def EveryLetter():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in a:
        print (letter)

def LettersAre():
    print("The Letters Are")

def Iterate():
    listA = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    listB = []
    for number in listA:
        listB.append(number/10)
    print(listB)


def SortNumbers():
    listA = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    listB = []
    listC = []
    listD = []
    for number in listA:
        if number>50:
            listB.append(number)
        elif number==50:
            listD.append(number)
        else:
            listC.append(number)
    print("Numbers Greater Than 50 Are")
    print (listB)
    print("Numbers Less Than 50 Are")
    print(listC)

SortNumbers()

def WhileLoop():
    counter = 0
    while counter<10:
        counter += 1
        print(counter)


WhileLoop()

class Person
    def_init_(self, name1, age1):
    self.name = name1
    
    age = 53

Person = Person()
print(Person.name)






