#This program is to help you to calculate the area and circumference of a circle and surface area and volume of a circle. All you need to do is to provide the radius of the circle 
pi = 3.142
r = int(input("Please input the radius of the circle: "))

area = (pi*(r**2))
print(f"The area of the circle is {area} cm(squared)") 

circum = (2*pi*r)
print(f"The circumference of the circle is {circum}cm")

s_area = 4*pi*r**2
print(f"The surface area of the sphere is {s_area}cm(square)")

s_volume = 4/3*(pi*r**3)
print(f"The volume of the sphere is {s_volume}cm(cube)")



#This program generates a 6 character long password for you using your first name and your year of birth
name =input("Enter your name: ")
year =input("Enter your year of birth: ")

import random
a=random.choice(name)
b=random.choice(year)
c=random.choice(name)
d=random.choice(year)
e=random.choice(name)
f=random.choice(year)

print("Your generated password is "+(a)+(b)+(c)+(d)+(e)+(f))