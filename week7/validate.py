import re

email = input("What's your email?: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")








# email = input("What's your email?: ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

#____________________________________________

# email = input("What's your email?: ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")