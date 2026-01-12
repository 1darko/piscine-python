import sys


try:
    if len(sys.argv) < 2:
        print()
        exit(1)
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert (sys.argv[1].isdigit()
            or ((sys.argv[1] and sys.argv[1][0] == '-')
                and sys.argv[1][1:].isdigit())), "argument is not an integer"
    if (int(sys.argv[1]) % 2 == 0):
        print("I'm even\n")
    else:
        print("I'm odd\n")
except AssertionError as e:
    print(f"AssertionError: {e}\n")
    exit(1)
