import random
def guessGame(a,b,actual):
    guess = int(input(f"Guess a number between {a} and {b} :- "))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number :- "))
            nguess = nguess + 1
        else:
            guess  = int(input(f"Enter a smaller number :- "))
    print(f"you guessed the number in {nguess} guesses ")
    return nguess

if __name__ == '__main__':
    a = int(input("Enter the value of a :- "))
    b = int(input("Enter the value of b :- "))
    actual = random.randint(a,b)
    print("Player 1's turn")
    g1 = guessGame(a,b,actual)
    print("Player 2's turn")
    g2 = guessGame(a,b,actual)

    if g1 < g2:
        print("Player 1 won the match")
    elif g1 > g2:
        print("Player 2 won the match")
    else:
        print("It's a tie")