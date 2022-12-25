# lembda functions or anontmous functions
# def add(a,b):
#     return a+b
# print(add(4,5))
#
# # def minus(x,y):
# #     return x-y
# # print(minus(9,5))
#
# minus = lambda x,y : x-y
# print(minus(5,4))

#difficult to understand
#using short function

# def a_first(a):
#     return a[1]


a = [ [1,14], [5,6], [8,23] ]
# a.sort(key=a_first)
a.sort(key=lambda x : x[1])
# a.sort()
print(a)
