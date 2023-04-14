class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        print(self.name, self.type)

    def open(self):
        print("restorant is open")


def one():
    Res = Restaurant("My", "old")
    print(Res.name, Res.type)
    Res.describe()
    Res.open()


# one()


def two():
    o = Restaurant(1, "q")
    tw = Restaurant(2, "w")
    th = Restaurant(3, "e")
    o.describe()
    tw.describe()
    th.describe()


# two()


def three():
    class User():
        def __init__(self, fname, lname, age):
            self.fname = fname
            self.lname = lname
            self.age = age

        def describe(self):
            print(self.fname, self.lname, self.age)

        def welcome(self):
            print("hi", self.fname, self.lname)

    J = User("After", "William", 31)
    K = User("Kserf", "Wenchery", 45)
    J.describe()
    K.describe()
    J.welcome()
    K.welcome()


three()
