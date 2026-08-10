def main():
    t = input("Input: ")
    for c in t:
        if c.lower() not in "aeiou":
            print(c, end="")
    print()
            
if __name__ == "__main__":
    main()