x = input("введите строку: ")


def counter(string: str):
    symbol = ""
    count = 0
    output = ""
    for i in string:
        try:
            int(i)
        except ValueError:
            if symbol == "" or symbol == i:
                symbol = i
                count += 1
            else:
                output += symbol + str(count)
                count = 1
                symbol = i
        else:
            print("Не вводите числа")
            quit()
    output += symbol + str(count)
    return output


out = counter(x)
print(out)
