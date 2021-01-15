import random
def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b} : "))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Please Enter a bigger number : "))
            nguess += 1
        else:
            guess = int(input(f"Please Enter a smaller number : "))
            nguess += 1

    print(f"\nWow !! You guessed the number in {nguess} Chances !!\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    actual1 = random.randint(a, b)
    print("Player 1's turn : \n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn : \n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print(f"Great !! Player 1 won the match with {g2-g1} Points $$\n")

    elif g1 > g2:
        print(f"Great !! Player 2 won the match with {g1-g2} Points $$ \n")

    else:
        print("OOPS !! Match Tie !!\n")


