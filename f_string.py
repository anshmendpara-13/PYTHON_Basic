# f_string

import math

me = "ansh"
a1 = 13

# a ="this is %s %s" % (me,a1)
# print(a)

# a = "this is {} {}"
# b = a.format(me,13)
# print(b)

a = f"this is {me} {a1} {math.sin(45)}"
print(a)
