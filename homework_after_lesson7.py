file = open("decfile.txt", "r+")
word = str(file.read()).lower()
choice = input("encode or decode? ").lower()

def encode(word):
    encoword = ""
    m = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    falphabet = "cdefghijklmnopqrstuvwxyzab"
    for x in word:
        m = alphabet.find(x)
        if x not in alphabet:
            encoword += " "
        else:
            encoword += falphabet[m]
    return encoword


def decode(encoword):
    word = ""
    m = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    falphabet = "cdefghijklmnopqrstuvwxab"
    for x in encoword:
        m = falphabet.find(x)
        if x not in falphabet:
            word += " "
        else:
            word += alphabet[m]
    return word


if choice == "encode":
    encoword = encode(word)
    print(encoword)
    file.write("\n" + encoword)
elif choice == "decode":
    encoword = encode(word)
    word = decode(encoword)
    print(word)
