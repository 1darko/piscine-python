import sys


def main():
    args = sys.argv
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
        'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '-----.', ' ': '/'
    }
    try:
        assert len(args) == 2, "AssertionError: incorrect number of arguments"
        msg = args[1].upper()
        assert all(c.isalnum() or c.isspace() for c in msg), \
            "AssertionError: 1st arg is not an alnum str"
        print(" ".join(MORSE_CODE_DICT[c] for c in msg))
    except AssertionError as msg:
        print(msg)
        return 1
    return


if __name__ == "__main__":
    main()
