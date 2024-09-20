#ASS-3

#1Assignment 1: Even or Odd Number 
# Task: Write a Python program that takes an integer input from the user and checks whether the number is even or odd using an if-else statement.

no=int(input("enter a number: "))
if no%2==0:
    print("your number is even.")
else: 
    print("your number is odd.")

#Assignment 2: 
# Task: Write a Python program that takes two numbers and an operator (+, -, *, /) as input. Perform the corresponding arithmetic operation and display the result using if-else conditions.

num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
ch=input("enter a opretor: ")
if ch == '+':
    print("sum is:",num1+num2)
elif ch == '-':
    print("sub is:",abs(num1-num2))
elif ch == '*':
    print("mul is:",num1*num2)
elif ch == '/':
    print("div is:",num1/num2)
else:
    print("ans is invelide...")

#Assignment 3: Check Leap Year
# Task: Write a Python program that asks the user to input a year. Check if the year is a leap year using if-else and print an appropriate message.
 
year=int(input("enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("this is a leap year...")
else:
    print("this is a not leap year...")
     
#Assignment 4: Vowel or Consonant
# Task: Write a Python program to check whether a given character is a vowel or a consonant using if-else statements. Consider both uppercase and lowercase inputs.

ch = input("Enter a alphabet:")
ch = ch.lower()
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print("It's vowel")
else:
    print("This's consonent")

#Assignment 5: Grade Calculator
# Task: Write a Python program that takes marks of five subjects as input and calculates the average. Then, assign a grade based on the average using if-else statements (e.g., A for 90+, B for 80-89, etc.).

mark=int(input("enter a marks: "))
if(mark<=100 and mark>=90):
    print("This is A Grade...")
elif(mark<=89 and mark>=80):
    print("This is B Grade...")
elif(mark<=79 and mark>=70):
    print("This is C Grade...")
elif(mark<=69 and mark>=60):
    print("This is D Grade...")
elif(mark<=59 and mark>=35):
    print("This is E Grade...")
else:
    print("This is Falled...")

#Assignment 6: Maximum of Three Numbers
# Task: Write a Python program to find the maximum of three numbers using if-else conditions.

num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
ans = 0;
if num1>num2 and num1>num3:
    print("num1 is greater than num2 and num3")
elif num2>num1 and num2>num3:
    print("num2 is greater than num1 and num3")
else:
    print("num3 is greater than num1 and num2")
     
#Assignment 7: Check Data Type
# Task: Write a Python program that accepts any input from the user and checks the data type of the input using if-else. Print whether it's an integer, float, string, or something else.

#Assignment 8: Positive, Negative, or Zero
# Task: Write a Python program that asks the user to input a number and checks if the number is positive, negative, or zero using if-else conditions.

num=int(input("enter a number: "))
if 0<num:
   print("this number a positive....")
elif 0>num:
   print("this number a negative....")
else:
   print("this number a 0....")
    
#Assignment 9: Check Divisibility
# Task: Write a Python program that takes an integer input and checks if it is divisible by 5 and 11 using if-else. Print appropriate messages based on the result.

num=int(input("enter a number: "))
if num%5==0 and num%11==0:
    print("this number are 5 and 11 divisibel...")
else:
    print("this number are not divisibel 5 and 11...")
     
#Assignment 10: Simple Login System
# Task: Write a Python program that simulates a simple login system. The program should ask for a username and password. Use if-else to check if the credentials match a predefined username and password and print a welcome message if they do. Otherwise, print an error message.
    
user_name="sunil parmar"
password=123
ent_username=input("enter a your name: ")
ent_password=int(input("enter a password: "))
if user_name == ent_username and password ==  ent_password:
    print("welcome to sunil parmar. your succesfuly to login...")
else:
    print("sorry, plesea cheked your name and password...!")