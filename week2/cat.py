def main():
    number =get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")

main()






#loop breaking and ask for input to print meow n times
# while True:
#     n = int(input("What's n?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")




#Being a little pythonic by exploiting print function
#print("meow\n" * 3, end="")


# how to loop with for function
# for _ in range (3):
#     print("meow")


# Counting up from 0 to 2
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


#Counting down from 3 to 1
# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1