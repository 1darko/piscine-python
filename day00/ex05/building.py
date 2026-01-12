import sys


def countAndPrint(building_name):
    """
    Count and print the number of upper case letters, lower case letters,
    digits, special characters and spaces in the given building name.
    """
    size = len(building_name)
    all = {
        "upper": 0,
        "lower": 0,
        "digits": 0,
        "special": 0,
        "spaces": 0
    }
    print(f"Analyzing text: {building_name}")
    for char in building_name:
        if char.isupper():
            all["upper"] += 1
        elif char.islower():
            all["lower"] += 1
        elif char.isdigit():
            all["digits"] += 1
        elif char.isspace() or char == '\r':
            all["spaces"] += 1
        else:
            all["special"] += 1
    print(f"The text contains {size} caracters.")
    print(f"{all['upper']} upper letters")
    print(f"{all['lower']} lower letters")
    print(f"{all['special']} punctuation marks")
    print(f"{all['spaces']} spaces")
    print(f"{all['digits']} digits")


def main():
    """
    Main function to handle input and call counting function.
    """
    try:
        assert (len(sys.argv) <= 2), "more than one argument is provided"
        if len(sys.argv) < 2 or not sys.argv[1]:
            try:
                build = input("What is the text to count?\n")
            except (EOFError):
                raise AssertionError("no input provided (EOF encountered).")
            except (KeyboardInterrupt):
                raise AssertionError("no input provided (KeyboardInterrupt).")
            assert build, "no building name provided."
        else:
            build = sys.argv[1]
        countAndPrint("\n" + build)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()
