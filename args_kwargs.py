# *args and **kwargs
# def function_name_print(a, b, c, d):
#     print(a,b,c,d)
# function_name_print("ansh","harshit","meet","prit")

def funarge(normal,*args,**kwargs):
    print(normal)
    #first normal ,second *args ,**third kwargs
    # print(args[0])
    for item in args:
        print(item)
    print("how i would like to introduce some of our heroes")
    for key, value in kwargs.items():
         print(f"{key} is a {value}")
         print(type(args))
# this always read in taple
har = ["ansh","meet","harshit","rohit","prit","om"]
normal = "this is a normal argument"
#this is dictionary
kwargs = {"ansh":"programmer","meet":"jocker","harshit":"fitness instructor"}
print(type(har))
funarge(normal,*har,**kwargs)



