import sys


NESTED_MORSE = { "A":".-", "B":"-...",
                    "C":"-.-.", "D":"-..", "E":".",
                    "F":"..-.", "G":"--.", "H":"....",
                    "I":"..", "J":".---", "K":"-.-",
                    "L":".-..", "M":"--", "N":"-.",
                    "O":"---", "P":".--.", "Q":"--.-",
                    "R":".-.", "S":"...", "T":"-",
                    "U":"..-", "V":"...-", "W":".--",
                    "X":"-..-", "Y":"-.--", "Z":"--..",
                    "1":".----", "2":"..---", "3":"...--",
                    "4":"....-", "5":".....", "6":"-....",
                    "7":"--...", "8":"---..", "9":"----.",
                    "0":"-----", " ":"/"}

def main():
    """This program translate the argument given into morse code if there is only alnum characters"""
    assert len(sys.argv) == 2, "1 argument needed"
    try:
        assert sys.argv[1].isalnum, "argument must contains only alphanumeric characters"
        string = sys.argv[1].upper()
        res = ""
        for c in string:
            if c in NESTED_MORSE.keys():
                res += NESTED_MORSE[c]
                res += " "
        print(res.removesuffix(" "))
    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()