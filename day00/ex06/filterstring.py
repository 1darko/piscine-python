import sys
from ft_filter import ft_filter


def main():
    """
    Filters words from a given string based on their length.
    Only words longer than the specified size are retained.
    1st argument: string of words separated by spaces
    2nd argument: integer size
    """
    args = sys.argv
    try:
        assert len(args) == 3, "incorrect number of arguments"
        # assert args[1], "first argument is an empty string"
        try:
            size = int(args[2])
            words = args[1].split(" ")
            it = ft_filter(lambda x: len(x) > size, words)
            print(list(it))
        except ValueError:
            raise AssertionError("2nd arg is not an integer")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return 1
    return


if __name__ == "__main__":
    main()
