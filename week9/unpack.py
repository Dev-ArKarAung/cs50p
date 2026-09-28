def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)









#     print("Positional:", args)
# f(100, 50, 25)

#########################################

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(**coins), "Knuts")
#########################################

# **coins is equivalent to  - coins["galleons"], coins["sickles"], coins["knuts"]
#########################################

# * before variable will unpack the list
# coins = [100, 50, 25]
# print(total(*coins), "Knuts")
#########################################

#Simple unpacking with split
# first, _ = input("What's your name? ").split(" ")
# print(f"hello {first}")