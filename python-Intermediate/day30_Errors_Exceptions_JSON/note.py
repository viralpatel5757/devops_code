# FileNotfound Error

try:
    file = open("hello.txt")
    key = {"key": "value"}
    print(key["key"])
except FileNotFoundError:
    file = open("hello.txt", "w")
    file.write("something !!")
except KeyError as error_message:
    print(f"key {error_message} was not found")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    raise TypeError # we can manually raise the error if we want to using raise keyword

# ------------- Example -------------------

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError :
        print("fruit pie")
    else:
        print(fruit + " pie")


make_pie(2)

