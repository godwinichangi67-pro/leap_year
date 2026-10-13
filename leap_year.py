import sys

def leapYear(year):
    if(year%4 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
year = int(sys.argv[1])
leapYear(year)
