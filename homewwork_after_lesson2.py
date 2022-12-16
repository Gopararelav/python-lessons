def one():
    while True:
        try: 
            x = float(input("впишите число: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print(x)
    for y in range(2):
        x += 1
        print(x)
# one()


def two():
    while True:
        try: 
            x = float(input("введите число 1: "))
            y = float(input("введите число 2: "))
            z = float(input("введите число 3: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print(x + y + z)
# two()


def three():
    while True:
        try: 
            FV = float(input("введите длину ребра куба: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print("Объём куба =", FV ** 3)
    print("Площадь полой поверхности =", 6 * FV ** 2)
# three()


def four():
    while True:
        try: 
            a = float(input("введите число a: "))
            b = float(input("введите число b: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print(3 * (a + b) ** 3  +275 * b ** 2 -127 * a -41)
# four()


def five():
    while True:
        try: 
            x = int(input("введите число: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print("число после ", x, "равно", x + 1)
    print("число перед ", x, "равно", x - 1)
# five()


def six():
    while True:
        try: 
            mouse = int(input("введите стоимость мыши: "))
            sysblock = int(input("введите стоимость системного блока: "))
            monitor = int(input("введите стоимость монитора: "))
            keyboard = int(input("введите стоимость клавиатуры: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print("стоимость трёх таких компьютеров равна:", (monitor + mouse + sysblock + keyboard) * 3)
# six()


def seven():
    while True:
        try: 
           x = int(input("введите число x: "))
           y = int(input("введите число y: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print(x, "+", y, "=", x + y)
    print(x, "-", y, "=", x - y)
    print(x, "*", y, "=", x * y)
# seven()


def egg():
    while True:
        try: 
           d = int(input("введите число d: "))
           n = int(input("введите число n: "))
           a = int(input("введите число a: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print(a + d * (n - 1))
# egg()



def nine():
    while True:
        try: 
            x = int(input("введите число x: "))
        except ValueError:
            print("не подходит!")
        except UnboundLocalError:
            print("не подходит!")
        else:
            break
    print(x, x * 2, x * 3, x * 4, x * 5, sep="---")
# nine()
