import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

a = ['1','2','3','4','5','6','7','8','9','0']
b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
c = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d = [',','!','@','#','$','%','^','&','*','(',')','_',"'",'"','+','{','}','|',':','<','>','?','~','`','-','=','[',']',";","'",'.','/']
i = random.randint(0,(len(d)-1))
j = random.randint(0,(len(b)-1))
k = random.randint(0,(len(c)-1))
l = random.randint(0,(len(a)-1))
m = random.randint(0,(len(d)-1))
password = (d[i]+b[j]+c[k]+a[l]+d[m] )
print(color.PURPLE + password + color.END)