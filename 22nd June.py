name=input("Enter your name: ") 
Age=int(input("How old are you?: "))
print(f"Hello, {name}, it seems you're {Age} years old")

name=input("enter your name: ")
Age=int(input("how old are you?: "))
print(f"Hello,{name}, it seems you're {Age} years old")

name=input("Enter your name: ")
print(f"Hi {name}, how old are you?: ")
Age=input()
print(f"So you're {Age} years old") 

name=input("Enter your name: ")
print(f"Hi{name},how old are you?: ")
Age=input()
print(f"so you are {Age} years old")
# This program calculates the area of a circle

pi = 3.142
r = int(input("Please input the radius of the circle: "))

area = (pi*(r**2))

print(f"The area of the circle is {area} cm(squared)") 


import time
delay=int(input("Please tell me how long you want me to sleep: "))
time.sleep(delay)
print("Hey, I'm awake")


#Continuation

import time
print("This is printed immediately")
time.sleep(2) #2 secs pause
print(f"this is printed after 2 secs")
import random
num = random.randint(1,100)
print(num)

import random
name =("Ayomide")
print(random.choice(name))

import random
name = input("Enter your name : ")
#selects randomly 
random_letter

#This is practicing random.choice
#This is to create a 4 character password
import random
month=input("Enter your month of birth: ")
name=input("Enter your name: ")

a=random.choice(month)
b=random.choice(name)
c=random.choice(name)
d=random.choice(month)

print("Your generated password is "+(a)+(b)+(c)+(d))

#This was the error I encountered 
import random
name =("Ayomide")
year =int 123456 

a=random.choice(name)
b=random.choice(year)
c=random.choice(name)
d=random.choice(year)
e=random.choice(name)
f=random.choice(year)

print("Your generated password is "+(a)+(b)+(c)+(d)+(e)+(f))