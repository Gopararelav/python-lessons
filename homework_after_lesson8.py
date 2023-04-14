print("hello user")
# licns = input("did you have license?: ").lower()
licns = "yes"
if licns == "yes":
    # name = input("What`s you`r name?: ").title()
    file = open("licenusers.txt", "r", encoding="UTF-8")
    licstr = str(file.read())
    print(licstr)
    lickkey = {}
    new = ""
    
    for x in licstr:
        if x == ":" or ",":
            print(new)
            new = ""

        new = new + x
elif licns == "no":
    pass
