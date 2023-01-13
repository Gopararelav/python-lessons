# def one():
#     x = []
#     while True:
#         y = ((input("введите число или x, чтобы начать подчёт: ")))
#         if y == "x":
#             break
#         else:
#             x.append(int(y))
#             print(x)
#     for y in x:
#         print(y)
#         понятия не имею, что делать
# one()


def two():
    new = ""
    old = []
    repeatnum = []
    z = list(input("числа: "))
    for number in z:
        if number == " ":
            old.append(new)
            new = ""
        else:
            new = new + number
    old.append(new)
    for cur in old:
        if cur not in repeatnum:
            repeatnum.append(cur)
    print(repeatnum)


# two()


def three():
    s = "In 2010, someone paid 10k Bitcoin for two pizzas."
    print(s[:12])
    print(s[::7])
    print(s[-9:])
    print(s[::-1])


# three()


def four():
    text = input("введите текст: ")
    print(len(text))
    print(text[0])
    print(text[:3])
    print(text[-3:])
    print(text[::-1])
    print(text[1:][:-1])
    for p in range(3):
        print(text, end="")


# four()


# def five():
#     m = []
#     text = input("введите текст: ")
#     textlist = list(text)
#     print(text)
#     textl = len(textlist)
#     for x in (textl / 2):
#         m.append(x)
#     print(m)
    # Не работает

# five()


def six():
    z = []
    while True:
        b = int(input("числа: "))
        if b == 0:
            break
        else:
            z.append(b)
    z.sort()
    print(z)


# six()


def seven():
    z = []
    while True:
        b = int(input("числа: "))
        if b == 0:
            break
        else:
            z.append(b)
    z.sort(reverse=True)
    print(z)


# seven()


def eight():
    z = []
    while True:
        b = (input("слова: "))
        if b == "":
            break
        elif b not in z:
            z.append(b)
            print(z)
    print(z)


eight()
