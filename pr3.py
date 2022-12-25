print("Enter the numbers of the list one by one\n")
size = int(input("Enter size of list :- "))
mylist = []

for i in range(size):
    mylist.append(int(input("Enter list element : ")))
print(f"your list is {mylist}")

# slicing tech method 1 and 2
reverse1 = mylist[::]
reverse1.reverse()
reverse2 = mylist[::-1]
print(f"My First reversed list of {mylist} is {reverse1}")
print(f"My Second reversed list of {mylist} is {reverse2}")

# third method is temp to reverse the list
reverse3  = mylist[::]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i]
    # print(f"the receersed list at i={i} is {reverse})"


print(f"Third reversed list of {mylist} is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three method gives same result")