a = str(input())
b = str(input())
count  = 0
d = []
start = 0
astart = 0
for i in range(len(b)):
    d.append(b[i])
# print(len(a))
# print(a[astart+1])
c = []


for i in range(len(a+b)):
    if((b[start]==a[astart])):
        for j in range(astart,len(b)):
            c.append(b[j])
            if (d==c):
                count = count + 1
                c.clear()
                astart = astart + 1
    else:
        astart = astart + 1
        # count = count


print(count)


