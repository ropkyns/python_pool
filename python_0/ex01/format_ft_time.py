import time

now = time.time()
today = time.strftime("%B %d %Y")

print("Seconds since January 1, 1970: ", "{:,}".format(now), "or " "{:.2e}".format(now), " in scientific notation")
print(today)