name = input("File name: ")

if name.endswith(".py"):
    print("text/x-python")
elif name.endswith(".jpg") or name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
else:
    extension = name.split(".")[-1]
    print("application/" + extension)