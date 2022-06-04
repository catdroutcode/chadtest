import sys
from termcolor import colored, cprint
from sys import platform

arch = colored("Do you use Arch Linux? ", "blue")
chad = colored("you are a chad!!!! ", "green")
soy =  colored("You are a soydeveloper! ", "magenta")


print(" ___  _           _    _               _   ")
print("|  _]| |_  ___  _| | _| |_  ___  ___ _| |_ ")
print("| [__| . |[_] |/ . |  | |  / ._][_-[  | |  ")
print("`___/|_|_|[___|\___|  |_|  \___./__/  |_|  ")


if platform == "linux" or platform == "linux2":
    basedornot = input(arch)
if basedornot == "yes":
    print(chad)
elif basedornot == "no":
    print(soy)
elif platform == "darwin":
    print(soy)
elif platform == "win32":
    print(soy)





                                           
