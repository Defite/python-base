#! /usr/bin/env python


def say_name():
    """
    Asks for name and print it
    """
    name = input("Name: ")
    print(name)


# say_name()

def add(num1=1, num2=2):
    return num1 + num2

# sum = add()

# print("Sum is {0}".format(sum))


def madlibs(name, noun="sneakers", adjective="red"):
    return "{0} has {1} {2}".format(name, adjective, noun)


madlib = madlibs("Nik", "shoes", "black")
print(madlib)
