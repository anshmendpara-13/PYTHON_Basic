# maps, filter and reduce

# numbers = ["54", "5", "13", "10"]

# print(map(int,numbers))
# numbers = list(map(int,numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2] + 13
# print(numbers[2])

# def sq(a):
#     return a*a
# num = [2,5,4,13,10,45,12]
# square = list(map(sq,num))
# print(square)

# num = [2,5,4,13,10,45]
# square = list(map(lambda x : x*x,num))
# print(square)


# def number(a):
#     return a
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# num = [1,2,3,4,5,6,7,8,9,10]
# func = [number, square, cube]
# for i in (num):
#     val = list(map(lambda x : x(i), func))
#     print(val)


# list_1 = [1,2,3,4,5,6,7,8,9,10]
# def is_greater_5(num):
#     return num>5
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)



# from functools import reduce

# list = [1,2,3,4,5]

# num = reduce(lambda x,y : x*y, list)
# print(num)

# num = 0
# for i in list:
#     num = num + i
# print(num)


