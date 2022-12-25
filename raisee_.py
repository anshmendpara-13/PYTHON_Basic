# a = input("What is your name : ")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"hello {a}.")

# task write about 2 built in exception

c = input("Enter your name : ")
try:
    print(a)
except Exception as e:
    if c == "ansh":
        raise ValueError("ansh is blocked he is not allowed")
    print("Exception handled")