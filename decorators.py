# decorators
# def function1():
#     print("call my name")
# fun2 = function1
# del function1
# fun2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a = funcret(0)
# print(a)

# def executor(func):
#     func("ansh")
# executor(print)

def dec1(func1):
    def nowexec():
        print("\t\t\t💕💕💕")
        func1()
        print("\t\t\t💕💕💕")
    return nowexec
@dec1
def who_is_ansh():
    print("ansh is good and chill mind boy")
# who_is_ansh = dec1(who_is_ansh)
who_is_ansh()