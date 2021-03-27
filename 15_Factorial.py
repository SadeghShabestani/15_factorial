import math
import termcolor2

number = int(input("Enter Number:"))

while True:
    if number > 0:
        result = math.factorial(number)
        print(termcolor2.colored(f"*Yes* Factorial: {result}", color="green"))
        break
    else:
        print(termcolor2.colored(f"*No* It Is Not Factorial : {number}", color="red"))
        number = int(input("TryAgain!! Enter Number:"))




