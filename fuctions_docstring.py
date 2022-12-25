#functions
# a = 5
# b = 6
# c = sum((a,b)) #built in function
# print(c)

#function make by def key word
def function1(a, b):
    print("hello you are in function1",a+b)
function1(3,4)

def function2(a,b):
    """This is function which ill calculate average of two numbers"""
    average = (a+b)/2
    return average
print(function2.__doc__)
v = function2(5,6)
print(v)