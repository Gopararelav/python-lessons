import base64

x = input("code: ")
x = bytes(x, "utf-8")
print(base64.b64encode(x))
x = base64.b64encode(x)
print(base64.b64decode(x))
