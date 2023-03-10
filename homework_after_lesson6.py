import names


def binser(name: "list", sernam):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabetk = {}
    number = 0
    sernum = []
    for x in list(alphabets):
        alphabetk[number] = x
        number += 1
    # print(alphabetk)
    for x in sernam:
        for num, sim in alphabetk.items():
            if x == sim:
                sernum.append(str(num))
                # print(sernum)
    name.sort()
    low = 0
    high = len(name)-1
    while low <= high:
        mid = (low + high)
        guesna = name[mid]
        # print(guesna)
        guesnu = []
        for x in guesna:
            for num, sim in alphabetk.items():
                # print(x, sim)
                if str(x) == str(sim):
                    guesnu.append(str(num))
                    # print(guesnu, sernum)
        if guesnu == sernum:
            return mid
        elif guesnu > sernum:
            high = mid - 1
        else:
            low = mid + 1


name = []
for x in range(0, 128):
    name.append(names.get_first_name().lower())
print(name)
sernam = input("Введите имя: ")
iammadeit = binser(name, sernam)
print(name[iammadeit], iammadeit)
