'''
    Lesson: Variables and Data Types
    Author: Mr. Kalisz
    Date Created: Sept 16, 2024
    Date Last Modified: Sept 16, 2024
'''

# Assignment Statements
# Variable Assignment - Set a variable to a value
# Variable is on the left side of the assignment symbol

#Integers

num = 4

#floats

fracNum = 3.4

# Strings

word = "Hello there"

#Booleans

tOrF = True

#Variable Call
#Get the variable value back to reuse it
#Variable is Anywhere else but left of an assignment symbol it is variable call

print(num)
#Replaces the variable num with its most recent value

#Overwrite variables by assigning to them again
num = 3

print(num)

#Operations

#Addition (+)

print(3 + 4)

print(num + 10)

num = 3 + 7 #num has a value of 10

num = num + 15 #num has a value of 25
#num = 10 + 15
#Right is ALWAYS solved before assigning

#Subtration (-)

num = num - 10 #15

#Multiplication (*)

print(num * 15) #225
print(num * 3.5) #52.5
print(num * 3.0) #45.0

#when using an operation with a float, the answer will ALWAYS be a float
#When using an operation without a float (two integers) the answer will USUALLY be an integer

#Division (/) - Always a float answer

print(num / 15) #1.0
print(num / 10) #1.5

#Integer Division (Floor Division) (//)

print(num // 10) #1
#rounds down to the nearest whole number
#Converting to an integer

#Mod (%) - returns the remainder of the question, treating the % like a divsion symbol

num = 45

print(num % 15) #0
print(num % 4) #1