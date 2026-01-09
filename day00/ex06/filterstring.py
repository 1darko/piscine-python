import sys
from ft_filter import ft_filter


def main():
    args = sys.argv
    try:
        assert len(args) == 3, "AssertionError: incorrect number of arguments"
        assert all(args.isalpha() or args.isspace() for args in args), "AssertionError: 1st arg is not a string"
        try:
            size = int(args[2])
            words = args[1].split(" ")
            it = ft_filter(lambda x: len(x) > size, words)
            print(list(it))
        except ValueError:
            raise AssertionError("AssertionError: 2nd arg is not an integer")
    except AssertionError as msg:
        print(msg)
        return 1
    return


if __name__ == "__main__":
    main()
