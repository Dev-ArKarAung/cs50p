# at least two letters, maximum 6, letters and numbers only
#number must be in end, no period, spaces and punctuation
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if s[1].isdigit():
        return False

    digit_started = False
    for c in s:
        if c.isdigit():
            if not digit_started and c == "0":
                return False
            digit_started = True
        elif digit_started and c.isalpha():
            return False

    return True

if __name__ == "__main__":
    main()