#operators in python
# arithmetic operator
# assignment operator
# comparison operator
# logical operator
# indentity operator
# memberwise operator
# birwise operator

# arithmetic operator
print("5+3 is",5+3)
print("5-3 is",5-3)
print("5*3 is",5*3)
print("5/3 is",5/3)
print("5//3 is",5//3)
print("5**3 is",5**3)
print("5%3 is",5%3)   #give a remainder

# assignment operator
print("assignment operator")
x = 5
print(x)
x +=7
print(x)


y=5
print(y)
y %=2
print(y)

"""
x * = y  means x = x * y
other
+=
-=
*=
/=
==
%=
"""

#comparison operator
print("comparison operator")
i = 8
print(i == 8)
print(i == 5)
"""
=
!=
> & >=
< & <=
"""

#logical operator
print("logical operator")
a = True
b = False
print(a and a)
print(a and b)
print(a or b)

#identity operator
print("identity operator")
a = True
b = False
p = 5
q = 7
print(a is b)
print(p is not q)
print(p is q)

#membership operator
print("membership operator")
list = [23,25,"ansh","om",54,21,41]
print(32 in list)
print("ansh" in list)
print(41 in list)
# in & not in

#bitwise operator
#0 = 00
#1 = 01
#2 = 10
#3 = 11

print(0 & 1)
print(0 | 3)