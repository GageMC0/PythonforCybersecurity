#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created 

#Promt user for name
user_name = input ("What is your name? ")
user_name = "Gage"
#Print hello and user's name
print ("Hello {0}".format (user_name))

print(f"Hello {user_name}")

print ("Hello " + user_name)

print ("Hello again", user_name)

print (user_name +  " today is going to be a great day!")

age_input = input ("How old are you?")

age = int (age_input)
age_in_two_years = age + 2

print ("In two years you will be", age_in_two_years)
