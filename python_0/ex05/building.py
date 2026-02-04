import sys


def main():
    """program to print information on a text as :
    -number of characters
    -upper letters
    -lower letters
    -punctuation marks
    -spaces
    -digits
    Assertion error if there is more than one argument provided
    and ask for a text if there is no argument provided"""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            string = input("What is the text to count ?\n")
        else:
            string = sys.argv[1]
        characters = len(string)
        upper = sum(1 for c in string if c.isupper())
        lower = sum(1 for c in string if c.islower())
        punctuation = sum(c in ".,?!'/\"-`{`}*[]:;@()_“”«»’" for c in string)
        space = sum(1 for c in string if c.isspace())
        digit = sum(1 for c in string if c.isdigit())
        print(f"The text contains {characters} character:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    print(main.__doc__)
    main()
