"""An exercise in remainders and boolean logic."""

__author__ = "730409609"


# Begin your solution here...
x = int(input("Enter an int: "))

if x % 2 == 0 and not x % 7 == 0:
    print("TAR")

if x % 7 == 0 and not x % 2 == 0:
    print("HEELS")

if x % 2 == 0 and x % 7 == 0:
    print("TAR HEELS")

if not x % 2 == 0 and not x % 7 == 0:
    print("CAROLINA")