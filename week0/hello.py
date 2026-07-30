def main():
    name = input("What is your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)

main()







# First lesson of hello.py

# Ask user for their name 
#name = input("What's your name?").strip().title()

# split user's name into first name and last name
#first, last = name.split(" ")

# Remove whitespace from str and capitalize first letter
#name = name.strip().title() 

# Capitalize first letter of str 
# name = name.capitalize()

# Capitalize first letter of each word in str 
# name = name.title() 

# Say hello to user, sep = separator, end = what to print at the end of the line
#print("hello,", name, sep ="")
#print("hello, " + name)

#print("hello, ", end="")
#print(name)
# print(f"hello, {name}")
#print(f"hello, {first}")