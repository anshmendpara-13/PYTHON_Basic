f = open("ansh.txt","rt")  #rt is default ,tb is binary mode

print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())

# content = f.read()
# print(content)

# for line in f:
#     print(line,end="")

# content = f.read(500)
# print("1",content)
# content = f.read(4)
# print("2",content)

f.close()
