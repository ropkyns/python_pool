import sys


try:
    number = int(sys.argv[1])
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as error:
    print(f"AssertionError: {error}")
except ValueError:
    print("AssertionError: argument is not an integer")
except IndexError:
    pass
