# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
# print(ls)
#
# ls = [i for i in range(100) if i%3==0]
# print(ls)


# dictionary me {key:value}
# list me []
# tuple me ()


# dict1 = {i :f"item{i}" for i in range(1,5)  if i%1==0}
# dict1 = {i:f"item{i}" for i in range(1,6)}
# dict2 = {value:key for key,value in dict1.items()}
#
# print(dict1,"\n",dict2)

# dresses = [dress for dress in ["dress1", "dress2", "dress1",
#                                "dress1", "dress2", "dress1"]]
# print(dresses)

# generator
# even = (i for i in range(100) if i%2==0)
# print(type(even))
# # print(even)
# # print(even.__next__())
# # print(even.__next__())
# # print(even.__next__())
# # print(even.__next__())
# # print(even.__next__())
# for item in even:
#     print(item)


no_of_list = int(input("How many items add in a comprehension : "))
input_string = input("Enter a list element separated by coma : ")
list = input_string.split(",")
t = int(input("Which type of comprehension you use : \n 1.List comprehension :\n 2.Dictionary comprehension :\n 3.Set comprehension : \n --> "))
if t==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {f"item {i}":i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s = {i for i in list}
    print(s)
    print(type(s))

