"""
iterable - __iter__() or __getitem()
iterator - __next__()
iteration
"""

# for i in range(1,51):
#     print(i)

# def gen(n):
#     for i in range(n):
#         yield i
#         # return i
#
# g = gen (11)
# print(g)
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
#
# for i in g:
#     print(i)


# h = "ansh"
# print(iter(h))
# iter = iter(h)
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# for i in h:
    # print(i)


    # -: project :-


p = int(input("Enter the number you want to till print fibonacci serires : "))
q = int(input("Enter the number you want to till print factorial serires : "))
def fibonacci_gen(n):
    n1,n2 = 0,1
    count = 0
    if n<=0:
        # this is condition for ant user not enter negative number
        print("please enter a positive integer : ")
    elif n==1:
        print("Fibonacci sequence upto",n,":")
        yield n1
    else:
        # print("Fibonacci sequence : ")
        while count<n:
            yield n1
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


def factorial_gen(n1):
    fac = 1
    for i in range(n1):
        fac = fac * (i + 1)
    yield fac


# print(fibonacci_gen(p))
print("fibonacci_series of",p)
for i in fibonacci_gen(p):
    print(i,)
print("\n")
# print(factorial_gen(q))
for j in factorial_gen(q):
    print("factorial_series of",q,"is",j)