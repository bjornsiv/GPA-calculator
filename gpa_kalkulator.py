import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description = "Calculate your current GPA")
 
    # add argument
    parser.add_argument("-a", "--add", nargs = '3', metavar = ("string","num", "num"), type = int, help = "Adds a new entry to /Grades/grades.csv")
    
    # parse the arguments from standard input
    args = parser.parse_args()

    #Checks which argument was passed and runs the assosiated function
    if args.read != None:
        add(args)
    elif args.remove != None:
        remove(args)
    elif args.show != None:
        calculate(args)
    
def add():
    print("yay")

def remove():
    print("yay")

def calculate():
    print("yay")

if __name__ == "__main__":
    # calling the main function
    main()