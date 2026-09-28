def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()


 #uppercased = map(str.upper, words)

# uppercased = [] # for word in words: #     uppercased.append(word.upper())
##############################
#   yell("This is CS50")
# def yell(phrase):
#     print(phrase.upper())