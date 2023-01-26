def one():
    import time
    cost = 0
    name = ""
    name = input("введите своё имя: ")
    while True:
        age = 0
        age = input("введите свой возрас: ")
        if age == '':
            break
        else:
            if int(age) >= 65:
                cost += 18
            elif int(age) <= 2:
                pass
            elif int(age) <= 12:
                cost += 14
            else:
                cost += 23
    with open("Ticket.txt", "w", encoding="UTF-8") as file:
        file.write(f"**********{name}**********\n|Cost =\t{cost}|")
        file.write(f"\n|Time =\t{time.ctime()}|")
    print(cost)
    print(name)


# one()


def two():
    a = [10, 2, 5, 1, 8, 7]
    N = len(a)
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(a)


two()
