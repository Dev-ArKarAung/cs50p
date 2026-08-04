def main():
    print_square(3)


def print_square(size):

    #for each row in square
    for i in range(size):

        # #for each brick in row
                # for j in range(size):
        
                #     #print brick
                #     print("#", end="")
        
                # print()
        print_row(size)


def print_row(width):
    print("#" * width)

        
        

main()    










#______________________________ print out the width of ?

# def main():
#     print_row(4)


# def print_row(width):
#     print("?" * width)


# main()

#________________________________ print out the height of #

# def main():
#     print_column(3)


# def print_column(height):
#     print("#\n" * height, end="") #Version 1

#     # for _ in range(height): #Version 2
#     #     print("#")


# main()

#__________________________

# for _ in range(3):
#     print("#")