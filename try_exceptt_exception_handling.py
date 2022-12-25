print("Enter the first number:")
num1 = input()
print("Enter the second number:")
num2 = input()
try:
    print("sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)

    print("this line is very important")

    #try:
    #except Exception as e:
    #print(e)