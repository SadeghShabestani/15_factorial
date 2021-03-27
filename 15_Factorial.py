import termcolor2
number = int(input("Enter Number: "))

for i in range(1,number+1):
    if number % i ==0:
        number = number / i
if number==1:
    print(termcolor2.colored(f"This Is a Factorial Number" , color="green"))
else:
    print(termcolor2.colored(f"This Is Not a Factorial Number", color="red"))



