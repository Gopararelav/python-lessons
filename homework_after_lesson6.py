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
    cy = 0
    while low <= high:
        cy += 1
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
            return mid, cy
        elif guesnu > sernum:
            high = mid - 1
        else:
            low = mid + 1


name = []
for x in range(0, 128):
    name.append(names.get_first_name().lower())
print(name)
sernam = input("Введите имя: ")
try:
    fina, cy = binser(name, sernam)
except TypeError:
    print(None)
    quit()
print(name[fina], fina, cy)
