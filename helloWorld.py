guessNo = 0
guessLim = 9
actualNo=87
while (True) :
    print("Enter a number:")
    input1=int(input())
    if input1<87 and guessNo<guessLim:
        print("Increase")
        guessNo=guessNo+1
        print((guessLim-guessNo), "guesses left.")
    elif input1>87 and guessNo<guessLim:
        print("Decrease")
        guessNo = guessNo + 1
        print((guessLim - guessNo), "guesses left.")
    elif input1==actualNo and guessNo<guessLim:
        print("You guessed it right")
        break
    else:
        print("Game over")
        break
print("thank you fr joining the game")