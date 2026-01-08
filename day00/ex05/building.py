import sys


def countAndPrint(building_name):
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
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided\n")
    elif (len(sys.argv) < 2 or sys.argv[1] == ""):
        try:
            build = input("What is the text to count?\n")
        except EOFError:
            print("\nAssertionError: no input provided (EOF encountered).")
            return 1
        except KeyboardInterrupt:
            print("\nAssertionError: no input provided (KeyboardInterrupt).")
            return 1
        if (build is None or build == ""):
            print("AssertionError: No building name provided.")
            return 1
        countAndPrint("\n" + build)
    else:
        countAndPrint(sys.argv[1])
    return 0


if __name__ == "__main__":
    main()
