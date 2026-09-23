import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex pattern to match: 9 AM to 5:00 PM, 9:00 AM to 5 PM, etc.
    pattern = r"^(1[0-2]|0?[0-9])(:([0-5][0-9]))? (AM|PM) to (1[0-2]|0?[0-9])(:([0-5][0-9]))? (AM|PM)$"
    matches = re.search(pattern, s)
    if not matches:
        raise ValueError("Invalid Format")

    #Extract start time components
    start_hour = int(matches.group(1))
    start_min = matches.group(3) if matches.group(3) else "00"
    start_ampm = matches.group(4)

    #Extract end time components
    end_hour = int(matches.group(5))
    end_min = matches.group(7) if matches.group (7) else "00"
    end_ampm = matches.group(8) 

    #convert both times to 24 hour format
    start_24 = convert_to_24(start_hour, start_min, start_ampm)
    end_24 = convert_to_24(end_hour, end_min, end_ampm)

    return f"{start_24} to {end_24}"
    

def convert_to_24(hour, min, ampm):
    if ampm == "PM":
        if hour != 12:
            hour += 12
    else: 
        if hour == 12:
            hour = 0

    #format 2 digits(e.g 9 >> 09)
    return f"{hour:02}:{min}"        

if __name__ == "__main__":
    main()