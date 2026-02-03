import sys as sys

# assert len(sys.argv) < 2, "more than one argument is provided"


try:
	number = int(sys.argv[1])
	assert sys.argv[1] is not int, "argument is not an integer"
	if int(sys.argv[1]) % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
except AssertionError as error:
	print(error)