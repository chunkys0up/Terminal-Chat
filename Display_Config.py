import sys

# Detect windows
if sys.platform.startswith("win"):
    COLOR = "\033[38;2;0;255;0m"
    RESET = ""
else:
    COLOR = "\033[38;2;255;128;0m"
    RESET = "\033[0m"


# test function
def colored_text(text):
    print(f"{COLOR}{text}{RESET}")


# check if username is valid
def valid_username(question: str):
    username = input(question)
    while (len(username) < 3 or len(username) > 24):
        username = input("Enter a valid username from 3-24 characters: ")
    return username
