import random 

def main():
    level = get_level()
    random_num = random.randint(1, level)
    guess = get_guess(random_num)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            return level
        except ValueError:
            continue

def get_guess(random_num):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            elif guess < random_num:
                print("Too small!")
            elif guess > random_num:
                print("Too large!")
            else:
                print("Just right!")
                return
        except ValueError:
            continue

if __name__ == "__main__":
    main()
                    