##This program finds the roots of a quadratic equation
a=1
b=-3
c=2

import math
x1=(-b+math.sqrt((b**2)-4*a*c))/2*a
x2=(-b-math.sqrt((b**2)-4*a*c))/2*a

print(f"The roots of the equation are {x1} and {x2}")