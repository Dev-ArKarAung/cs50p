import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Look for src=" followed by optional http/https, optional www, youtube.com/embed/, 
    # and capture the video ID (alphanumeric characters, dashes, underscores)
    matches = re.search(r'src="(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if matches:
        #matches.group(1) holds the captured video ID
        video_id = matches.group(1)
        return f"https://youtu.be/{video_id}"
    
    return None





if __name__ == "__main__":
    main()