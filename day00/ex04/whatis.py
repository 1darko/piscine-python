import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided\n")
    exit(1)
elif len(sys.argv) < 2:
    print()
    exit(1)
if(sys.argv[1].isdigit()):
    if(int(sys.argv[1]) % 2 == 0):
        print("I'm even\n")
    else:
        print("I'm odd\n")
else:
    print("AssertionError: argument is not an integer\n")
    exit(1)