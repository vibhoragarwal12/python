#INTEGER

#name="vibhor"
#age = 23
#age +=1
#print(name+age)

#generates error file
## to print the age and name together we convert age to string by using str(age) 

#print(name+str(age))

#This is called type casting

#STRING

#first_name = "vibhor"
#last_name = "agarwal"
#Full_name = first_name+" "+last_name
#print("Hello "+Full_name)

#FLOAT

#height=245.4
#print(type(height))

#BOOLEAN

#human=True
#print(type(human)) gives class boolean

#MULTIPLE ASSIGNMENT

#name,age,attractive="vibhor",21,True
#print(name)
#print(age)
#print(attractive)

#if multiple variables have same value we can assign them using equals

# vibhor=shubham=shivam=30

# METHODS OF STRINGS

#name = "Bro code"

# print(len(name)) 
#prints length of string

# print(name.find("r"))
#used to find position of a letter in string

# print(name.capitalize()) 
#used to capitalize first letetr of string

# print(name.upper()) 
#use dto capitalize whole string

# print(name.lower())
#used to convert string in lower case

# print(name.isdigit())
#used to determine if the string is numbers

# print(name.isalpha())  
#used to know if the string is letter no spaces

#print(name.count("o"))
#determine the number of time a letter is repeated

#print(name.replace("the thing to be replaced","to be reblaced with"))
#used to replace

#print(name*3)
#used to print values as number of times we want

#TAKING INPUT IN PYTHON

#input()

#name=input("What is your name?: ")
#print("Hello "+name)
#by default input returns string
#to change it we have to use typecasting

#USING MATH LIBRARY AND ITS FUNCTIONS

# import math
#it is uesd to import the math library

# pi=3.4
# x=1
# y=3
# z=7
# print(round(pi))
#round off the number

# print(math.ceil(pi))
#rounds of the float number to upper limit

# print(math.floor(pi))
#round of the float number to lower limit

# print(abs(pi))
#displays how far the value is from zero(absolute value function)

# print(pow(pi,2))
# pow function is used to create power function

# print(math.sqrt(pi))
#square root function is used to find square root

# print(max(x,y,z))
# this fnctn is used to find max value out of all

# print(min(x,y,z))
# this fnctn is used to find max value out of all

#SLICING STRING

#(create a substring by extracting elements from another string)
# can be done using two fuctions indexing[] and slice() 
# [start:stop:step]

# name = "Vibhor agarwal"
# first_name = name[:6]
# last_name=name[7:]
# funky_name = name[::2]

# step will display only the characters skiiping the counts by default its value is 1 and if we put 2 it will display every alternate caharcter with 1st character as the same.

#for reversing the existing string just put the value of step to = -1 it will reverse the excisting string [::-1]

# print(funky_name)
# print(first_name)
# print(last_name)

# website1 = "http://google.com"
# website2 ="http://wikipedia.com"

# name=slice(7,-4)
# print(website1[name])

# syntax to use a slice function is object = slice(,) to use a slice function what we do is first we create a object and put the slice function inside it like the indexing and all and then we print the slice function by syntax as print(name of original string[slice object name])

# print(website2[name])

# CONDITIONAL STATEMENTS

# IF Statement

#age=int(input("how old are you?"))
# if age >= 18:
#   print("adult")
# else:
#   print("child")  

# LOGICAL OPERATOR

# temp = int(input("What is the temperature outside?;"))
# if temp>0 and temp<30: (and means both conditions must be true)
#  print("good to go")
# elif temp<0 or temp>30: (either one is true)
#  print("stay inside")
# not operator reverses the conditions

# LOOPS

# WHILE LOOP 

# a statement thatt will execute its block of code as long as its conditions remins true 

# while 1==1:
#   print("help im stuck in a loop")
 # exa,mple of infinitre loop
 
# name = "" / name = None
# while len(name) == 0: / while not name
#   name = input("Enter the name")
# print("hello" + name)  

# FOR LOOP

# for i in range(10):
#   print(i)

# for i in range(10,20):  / 10 is inclusive and 20 is exclusive 
#  print(i)

# name = "vibhor"
# for i in name:
#   print(i)

# for i in "vibhor":
#  print(i)

# import time
# for seconds in range(10,0,-2):
#   print(seconds)
#   time.sleep(3) # creates a time stamp or time delay 
# print("happy new year")  

# NESTED LOOPS (one loop inside the other loop)

# rows=int(input("no. of rows?"))
# column=int(input("no. of columns?"))
# symbol=input("enter the symbol?")

# for i in range(rows):
#   for j in range(column):
#     print(symbol, end=" ") # end is used to avoid jumping to next line
#   print()

# Loop CONTROL STATEMENTS

# break = use dto terminate the loop entirely
# continue = skip to the next iteration of loop
# pass = does nothing, acts as placeholder

# while True:
#   name=input()
#   if name !="":
#     break

# phone_number = "123-456-789"
# for i in phone_number:
#   if i == "-":
#     continue
#   print(i,end="")
  
# for i in range(1,21):
#   if i == 3:
#    pass
#   else:
#     print(i,end="")
    
# LIST

# used to store multiple items in a single variable

# food = ["pizza" ,"hamburger" ,"pasta" ,"hotdog"]
# food[0]="spaghetti"  # modifying list using index
# food.append("ice-cream") #modifies list and add to last 
# food.remove("hotdog") #remove the selected item
# food.pop() # removes the item from last index
# food.insert(0,"cake") #adds the item to given index but doesnot remove the previous item
# food.sort()  is used to sort a list
#fodd.clear()  is used the clear the list

# for i in food:
#   print(i)

# 2-D LIST list of lists

# drinks = ["whiskey", "vodka", "rum"]
# dinner = ["chicken", "hamburger", "pizza"]
# dessert = ["cake", "ice-cream"]

# food = [drinks,dinner,dessert]

# print(food[0][1])

# first index in food is from food list and second index is from the above three lists


# TUPLES  (collection which is ordered and unchangeable used to group related data together)

# student = ("rick",21,"male")
# print(student.count("rick")) #count the no. of times vaiable is present
# print(student.index("male")) #shows the index

# for i in student:
#   print(i)
# if "rick" in student: #checks if variable is present
#   print("rick is here")  

# SET (collection which is unordered, unindexed, no duplicates)

# utensils ={"fork","spoon","knife"}
# dishes = {"bowl","plate","cup","knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# utensils.update(dishes) updtes the set
# dinner_table = utensils.union(dishes) merges both sets
# print(utensils.difference(dishes)) prints the difference of sets
# print(utensils.intersection(dishes)) prints the common of both
# for x in utensils:
#   print(x)

# DICTIONARIES 
# (A changeable, unordered collection of unique key: value pairs) Fast because they use hashing, allow us to access a value quickly

# capitals = {'USA':'Washington Dc','India':'Delhi','Russia':'Moscow','China':'Beijing'}

# capitals.update({'Germany':'Berlin'}) updates the dictionary
# capitals.update({'USA':'Chicago'}) updates the value in existing dictionary
# capitals.pop('China') pops out or deletes key and value of given key
# capitals.clear() clears the dictionary

# print(capitals['Russia']) prints the value
# print(capitals.get('Germany')) check whether te key is present or not if not give output none
# print(capitals.keys()) prints all the keys in a given dictionary
# print(capitals.values()) prints all the values in the dictioanry
# print(capitals.items()) prints all the key and values

# for key,value in capitals.items(): for loop for printing key and value in dictionary
#   print(key,value)

# INDEX OPERATOR [] = gives access to a sequences element(str,list,tuples)

# name = 'vibhor Agarwal!'

# if(name[0].islower()):  checks if first letter is lowercase
#   name = name.capitalize()  converts first letter to capital

# first_name = name[0:6].upper() converts all chacter in uppercase
# last_name = name [7:].lower() converts all charater in lowercase
# last_character = name[-1]  -ve index used to access last element
# print(first_name)  
# print(last_name)
# print(last_character)

## ** FUNCTIONS ** ##
# Is a block of code which is executed only when it is called

# def hello():
#   print("hello")

# hello()  

# def hello(name):
#   print("hello "+name)
#   print("have a nice day")
# my_name = "vibhor"
# hello(my_name)

# def hello(f_name,l_name,age):
#   print("hello "+f_name+" "+l_name)
#   print("you are "+str(age)+" old")
# hello("vibhor","agarwal",21)

# ** RETUEN STATEMENT ** #

# Functions send python values/objects back to the caller. these values/objects are known as the function's return value

def multiply(number1,number2):
  result = number1*number2
  return result
print(multiply(3,4))
