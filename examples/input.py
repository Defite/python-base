#! /usr/bin/env python

name = input("Name: ")
job = input("Occupation: ")
location = input("Location: ")

print("Hey, {0}, being {1} in {2} must be exciting!".format(name, job, location));

response = input("Is it? ")

if response in ("yeah", "y", "yes"):
    print("How exciting!")
elif response in ("nope", "n", "no"):
    print("Sad to hear that :(")
else:
    print("Well, don't think I understand you...")
