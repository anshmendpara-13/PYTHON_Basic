#calculator
print("pleasse type in the math operation you would like to complete:\n")
print("1. + for additio")
print("2. - for subractio")
print("3. * for multiplicatio")
print("4. / for divisio")
print("5. ** for squre")
print("6. off the calculator\n")


print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())
print("\n")

sum=num1+num2
sub=num1-num2
mult=num1*num2
div=num1/num2
squre=num1*num1 and num2*num2


while(1):
    print("Enter your choice:")
    A=int(input())
    # print("\n")
    if A == 1:
        print("sum of two number is : ")
        print(num1+num2)
    elif A == 2:
        print("subtraction of two number is : ")
        print(num1-num2)
    elif A == 3:
        print("multiplication of two number is : ")
        print(num1*num2)
    elif A == 4:
        print("division of two number is : ")
        print(num1/num2)
    elif A == 5:
        print("squre of numbers are : ")
        print("fist number squre is :")
        print(num1*num1)
        print("second number squre is :")
        print(num2*num2)
    elif A == 6:
        print("-:you calculator is off:-")
        break
    else:
        print("your choise is invalid")
        print("try again")



