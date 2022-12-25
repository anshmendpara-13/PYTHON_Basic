# tell function = use for where the file pointer
# seek function = use for file pointer point this point which point you choise in seek function
f = open("ansh.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(0)
print(f.tell())
print(f.readline())
f.close()