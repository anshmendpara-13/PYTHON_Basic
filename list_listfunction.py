grocery = ["harpic","vim bar","deodrant","tamato","54","lollypop"]
#print(grocery)
# this start from 0 and so one...
numbers = [54,5 ,26 ,85 ,32]
#numbers.sort()
#numbers.reverse()
#print(numbers)        #short and reverse change original list
#print(numbers[3])
#slising
print(numbers[1:5:])
print(len(numbers))
print(max(numbers))
print(min(numbers))
#use append
#join number in last
numbers.append(4545)
print(numbers)
numbers.insert(2,13)
print(numbers)
#particular number remove
numbers.remove(13)
print(numbers)
#pop use for last number remove
numbers.pop()
print(numbers)
numbers[2]=25
print(numbers)
#mutable = can change
#immutable = can not change
#tp = (1,2,3)
#print(tp)
#tp1 =(1,)
#print(tp1)
#swap the numbers
a = 12
b = 21
a,b = b,a
print(a,b)






