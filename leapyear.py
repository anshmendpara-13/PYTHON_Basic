year = int(input())
x = int(year%4==0)
y = int(year%100!=0)
z = int(year%400==0)
if(int(x & (y|z)) ):
    print("true")
else:
    print("false")
