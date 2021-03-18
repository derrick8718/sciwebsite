#Instructs user to input what is being asked 
#Since input returns a string, int() converts the output back to an integer
x = int(input("What is the number? "))
 
#Operator that returns the remainder of the inputted number divided by 2 
#If remainder is equal to 0, print functions with help from f-strings display the number the user entered and that the number was even
if x % 2 == 0:
    print(f"Your number is: {x}") 
    print("This number is an even number.")
#If remainder is not equal to 0, print functions with help from f-strings display the number the user entered and that the number was odd
else:
    print(f"Your number is: {x}")
    print("This number is an odd number.")





