# recursive vs iterative approach
#n! = n * n-1 * n-2 * ...... * 1

# print("iterative approach")
# def factorial(n):
#     """
#
#     :param n: inreger
#     :return: n * n-1 * n-2 * ... * 1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
#
# number = int(input("Enter the number:\n"))
# print("factorial of",number,"is",factorial(number),end =".""\n")
#
# print("recursive approach")
# def factorial(n):
#     """
#
#     :param n: integer
#     :return: n * n-1 * n-2 * ... * 1
#     """
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# number = int(input("Enter the number:\n"))
# print("factorial of",number,"is",factorial(number),end =".""\n")

print("fibonacci")
# 0 1 1 2 3 5 8 13 21 ...
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number = int(input("Enter the number:\n"))
print("fibonacci of", number, "is", fibonacci(number), end=".""\n")
