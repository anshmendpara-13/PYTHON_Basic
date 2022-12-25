value = int(input())
if(value%2!=0):
    print("weird")
elif((value%2==0) & (2<=value<=5)):
    print("not weird")
elif((value%2==0) & (6<=value<=20)):
    print("weird")
elif((value%2==0) & (20<value)):
    print("not weird")