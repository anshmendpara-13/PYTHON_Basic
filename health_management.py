# health managment system
# 3 clients = ansh,harshit,romin
# def getdate():
#     import datetime
#     return datetime.datetime.now()

# def getdate():
#     import datetime
#     return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


#bhai ye rha program
import datetime
def getdate():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food : "))
        if(c==1):
            value=input("Type here :-\n")
            with open("Ansh-ex.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif(c==2):
            value = input("Type here :-\n")
            with open("Ansh-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif(k==2):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        if (c == 1):
            value = input("Type here :-\n")
            with open("Harshit-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("Type here :-\n")
            with open("Harshit-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif(k==3):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        if (c == 1):
            value = input("Type here :-\n")
            with open("Romin-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("Type here :-\n")
            with open("Romin-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Plz enter valid input (1(Ansh),2(Harshit),3(Ronim)")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food : "))
        if(c==1):
            with open("Ansh-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("Ansh-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        if (c == 1):
            with open("Harshit-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Harshit-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("Enter 1 for excersise and 2 for food : "))
        if (c == 1):
            with open("Romin-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Romin-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")
print("-: This is health management system :- ")
a=int(input("Press 1 for log the value and 2 for retrieve : "))

if a==1:
    b = int(input("Press 1 for Ansh 2 for Harshit 3 for Romin : "))
    take(b)
else:
    b = int(input("Press 1 for Ansh 2 for Harshit 3 for Romin : "))
    retrieve(b)