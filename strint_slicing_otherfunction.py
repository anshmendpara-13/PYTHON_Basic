#explore string
my = "my name is ansh"
print(my[0:15])
#string start from 0 and in a string last one not add so we add one more number
#using len use for string size
print(len(my))
#first defoult 0
#second defoult len of string
#third defoult 1
print(my[::])
#third is - so string ko ulti kaulata karake likhana he
print(my[::-1])
#first and second is - so counting in opposite direction and this same for counting forward direction

#boolien use
print(my.isalnum())
#space in string so false and not space in string so true
print(my.isalpha())
print(my.endswith("ansh"))
print(my.count("a"))
print(my.capitalize())
print(my.find("ansh"))
print(my.lower())
print(my.upper())
print(my.replace("ansh","neev"))