def main():
    x = get_int("What's x? ")
    print (f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass #silently ignore the error and repeat
            #print("x is not an integer") # print this if there's ValueError


main()
