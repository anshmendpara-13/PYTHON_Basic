s = set()
#print(type(s))
l = [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
print(type(s))             #use set
s.add(1)
s.add(2)
#s1 = s.union({5,6})

#s1 = s.union({1,2,3})
#print(s,s1)

s1 = {5,6}
print(s.isdisjoint(s1))
#s1 = s.intersection({1,2,3})
#print(s,s1)
#print(len(s))           #we use min ans max
#print(len(s1))

#print(s.isdisjoint(s1))
