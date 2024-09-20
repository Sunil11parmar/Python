#ass2

#1) Greeting Program: Write a program that asks the user for their name and then greets them with a personalized message.

en=input("enter a name: ")
print("hello",en,"your name is very nice...!!")

#2) Age Calculator : Create a program that prompts the user to enter their birth year and calculates their age.

birth_year=int(input("enter your birth year: "))
current_year=2024
age=current_year-birth_year
print("you are",age,"year old..!")

#3) Simple Math Quiz: Ask the user to input two numbers and then display their sum

val1=int(input("enter a value: "))
val2=int(input("enter a value: "))
ans=val1+val2
print("sum value is: ",ans)

#4) Temperature Converter: Write a program that converts a temperature from Celsius to Fahrenheit based on user input.

celsius=int(input("enter a number: "))
fahrenheit=celsius*(9/5)+32
print(fahrenheit)

#5) Favorite Color: Ask the user for their favorite color and then print a message incorporating their favorite color.

color=input("what is your favorite color: ")
print("your favorite color is:",color)

#6) Height Conversion: Create a program that asks the user for their height in meters and converts it to centimeters.

heightM=int(input("enter a value: "))
heightCM=heightM*100
print("heightCM is:",heightCM)

#7) Simple Interest Calculator: Prompt the user for the principal amount, rate of interest, and time period, and then calculate and display the simple interest.

p=int(input("what is the principle amount: "))
r=int(input("what is the rate of intrest: "))
t=int(input("what is the period of time: "))
si=p*r*t/100
print(si)

#8) Word Count : Write a program that asks the user to enter a sentence and counts the number of words in the sentence.

str=input("enter a messege: ")
words=str.split()
wordcount=len(words)
print("number of words in the sentence:",wordcount)

#9) Birthday Reminder: Ask the user for their birth date in the format (day/month) and print a reminder message.

birthday=input("enter your birth(day/month):")
print("your birthday is",birthday,"don't forget celebret...")

#10) Number Comparison: Create a program that prompts the user to enter two numbers and then determines and displays which number is larger.

val1=int(input("enter your value: "))
val2=int(input("enter your value: "))
if(val1>val2):
    print("val1 is greterthen val2")
else:
    print("val2 is greter than val1")
