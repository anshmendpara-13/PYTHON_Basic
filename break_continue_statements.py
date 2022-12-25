# breck and continue

# pyton file name not match moduls

# i=0
# while(True):        #while(1) and while(True) means loop run infinite
#
#     if i+1<7:             #if and loops ke bad semicolum ata he
#         i = i + 1
#         continue
#
#     print(i+1,end=" ")
#     if(i==15):
#         i = i + 1
#         break               #stop the loop
#     i = i +1

# question
while (True):
    i = int(input("Enter the number:\n"))
    if i > 100:
        print("congratulation you choise 100 pluse number")
        break
    else:
        print("try again")
        continue

