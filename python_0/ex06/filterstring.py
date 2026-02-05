import sys
from ft_filter import ft_filter


def words_count(word):
    """Return true if the len of the word given is higher or equal to the second argument given to the program"""
    if (len(word) >= int(sys.argv[2])):
        return True
    else:
        return False

def main():
    """This program pass the first argument given as a list to the function words_count with ft_filter and print the result as a list"""
    try:
        assert len(sys.argv) == 3, "2 arguments needed"
        assert type(sys.argv[1]) is str, "first argument must be a string"
        li = sys.argv[1].split(" ")
        number = int(sys.argv[2])
        assert type(number) is int, "sedonc argument must be an integer"
        print(list(ft_filter(words_count, li)))
    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()