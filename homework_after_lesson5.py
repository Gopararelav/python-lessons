def one():
    num1 = []
    while True:
        c = int(input("введите число 0 = окончанию ввода: "))
        if c != 0:
            num1.append(c)
        elif num1 == []:
            print("невозможно найти среднее значение угля")
            quit()
        else:
            break
    h = 0
    over = 0
    for x in num1:
        over += x
        h += 1
    print(over / h)


one()


def two():
    original = [4.95, 9.95, 14.95, 19.95, 24.95]
    for x in original:
        print("|$" + str(x), "$" + str(x-(x*0.6)), "$" + str(x*0.6), sep=",  ", end="|\n")


# two()

def CtoF():
    for x in range(1, 101):
        print("|C" + str(x), "=", "F" + str(((x*9)/5)+32), sep=" ", end="|\n")


# CtoF()
