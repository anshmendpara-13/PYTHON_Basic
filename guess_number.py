N=13
trail = 8
print("you gurss only 9 times")
while(trail>=0):
    # print("Enter your guess:")
    n = int(input("Guess the number : "))
    if n < N:
        print("Enter some big number")
    elif n > N:
        print("Enter some small number")
    else:
        print("you are won this game")
        print("--:congratulation:--")
        break
    print(trail,"trail left")
    trail = trail - 1
if(trail<0):
    print("-:GAME OVER:-")

