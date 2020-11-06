import time
print("hello \nmy name is Aman Malik and this is a rock , paper , scissors game that i made \nhope you like it \nplease "
      "visit my github profile amanm063 to see the more of these codes")
lose = "the computer has won the game.Try later"
win = "congratulation you have won!. Play again ."
lives = 5
score = 0
draw = 0
computer_lives = 5
while True:
    print("please fill these details:")
    name = input("Enter your name :").lower()
    time.sleep(0.5)
    print("welcome to the game {}".format(name))
    time.sleep(0.5)
    print("are you ready to play ")
    time.sleep(0.5)
    print("_______________    _______________  _______________      ")
    print("|    _____    |    |             |  |    __________|    ")
    print("|    |___|    |    |    _______  |  |    |__________     ")
    print("|             |    |    |_____|  |  |              |   ")
    print("|         ____|    |             |  |________      |        ")
    print("|    |\    \       |    _________|           |     |   ")
    print("|    | \    \      |    |            ________|     |   ")
    print("|    |  \    \   * |    |     *     |              | * ")
    print("|____|   \____\    |____|           |______________|       ")
    time.sleep(0.5)
    print("\n\n\n\nhere are some rules:")
    time.sleep(0.5)
    print("you get", lives, "and the computer gets", computer_lives)
    time.sleep(0.5)
    print(" to exit the game type exit and the game will close")
    time.sleep(0.5)
    print("all rules of the original rock , paper , scissors game remains the same")
    time.sleep(0.5)
    print("type rules to see all these rules again")
    time.sleep(0.5)
    print('good luck and have fun \nlet\'s see if you can beat the computer\n\n\n')
    while True:
        rps = input("rock,paper,scissors ?.........:").lower()
        import random

        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        # all rock statements
        if (rps == "rock") & (computer == "paper"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(lose)
            time.sleep(0.5)
            lives = lives - 1
            time.sleep(0.5)
            print("your remaining lives:", lives)
        if (rps == "rock") & (computer == "scissors"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(win)
            time.sleep(0.5)
            score = score + 1
            computer_lives = computer_lives - 1
            time.sleep(0.5)
            print("your score is :", score)
        if (rps == "rock") & (computer == "rock"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(draw)
            draw = draw + 1
            time.sleep(0.5)
            print("your remaining lives:", lives,
                  "\ntimes the game was a draw :", draw)

        # all scissors statements
        if (rps == "scissors") & (computer == "rock"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(lose)
            lives = lives - 1
            time.sleep(0.5)
            print("your remaining lives:", lives)
        if (rps == "scissors") & (computer == "paper"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(win)
            score = score + 1
            computer_lives = computer_lives - 1
            time.sleep(0.5)
            print("your score is :", score)
        if (rps == "scissors") & (computer == "scissors"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(draw)
            draw = draw + 1
            time.sleep(0.5)
            print("your remaining lives:", lives,
                  "\ntimes the game was a draw :", draw)

        # all paper statements
        if (rps == "paper") & (computer == "scissors"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(lose)
            lives = lives - 1
            time.sleep(0.5)
            print("your remaining lives:", lives)
        if (rps == "paper") & (computer == "rock"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(win)
            score = score + 1
            computer_lives = computer_lives - 1
            time.sleep(0.5)
            print("your score is :", score)
        if (rps == "paper") & (computer == "paper"):
            print("computer chooses:", computer)
            time.sleep(0.5)
            print(draw)
            draw = draw + 1
            time.sleep(0.5)
            print("your remaining lives:", lives,
                  "\ntimes the game was a draw :", draw)

        # other commands
        if rps == "rules":
            print("\n\n\n\nhere are some rules:")
            time.sleep(0.5)
            print("you get", lives, "and the computer gets", computer_lives)
            time.sleep(0.5)
            print(" to exit the game type exit and the game will close")
            time.sleep(0.5)
            print(
                "all rules of the original rock , paper , scissors game remains the same")
            time.sleep(0.5)
            print("type rules to see all these rules again")
            time.sleep(0.5)
            print(
                'good luck and have fun \nlet\'s see if you can beat the computer\n\n\n')

        # about the game's exit
        if lives == 0:
            time.sleep(0.5)
            print("thank you for playing \n your score is :", score, "\nyour had ", lives,
                  " remaining \nand the computer had ", computer_lives,
                  " lives remaining \nand the total draws were ", draw)
            stop = input("press enter to exit").lower()
            exit()
        if computer_lives == 0:
            time.sleep(0.5)
            print("thank you for playing \n your score is :", score, "\nyour had ", lives,
                  " remaining \nand the computer had no lives remaining \nand the total draws were ", draw)
            stop = input("press enter to exit").lower()
            exit()
        if rps == "exit":
            break
    else:
        time.sleep(0.5)
        print("sorry for the inconvenience , please try later")
