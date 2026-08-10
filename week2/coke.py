def main():
    total = 0
    while total < 50:
        print("Amount due: ", 50 - total)
        coin = int(input("Insert coin: "))
        if coin in [25, 10, 5]:
            total = total + coin
        
    print("Change owed: ", total - 50)        
 

if __name__ == "__main__":
    main()