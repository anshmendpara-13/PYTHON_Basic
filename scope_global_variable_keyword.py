# l = 10  #global
# def  function1(n):
#     # l=5 #local
#     m=45 #local
#     global l
#     l = l*5
#     print(l,m)
#     print(n,"i have printed")
#
# function1("this is me")
# print(l)

#you make global variable so you not change global variable
#if you change global variable so you print global key word and variable =  global l
#and this time not make local variable
#you make local variable so you change

def ansh():
    x = 10
    def meet():
        global x
        x = 88
    print("before calling meet()",x)
    meet()
    print("after calling meet()",x)
ansh()
print(x)