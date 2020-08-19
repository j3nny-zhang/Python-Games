import random

def main():
    player1 = 0
    player2 = 0
    rounds = 1
    player1Score = 0
    player2Score = 0

    while rounds !=11:
        #dice roll
        print("-------------")
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Rolls: " + str(player1))
        print("Player 2 Rolls: " + str(player2))


        if player1 > player2:
            print("...")
            print("Player 1 wins this round!")
            print("...")
            player1Score = player1Score + 1
            print("Player 1 has " + str(player1Score) + " points!")
            print("Player 2 has " + str(player2Score) + " points!")
        elif player1 < player2:
            print("...")
            print("Player 2 wins this round!")
            print("...")
            player2Score = player2Score + 1
            print("Player 1 has " + str(player1Score) + " points!")
            print("Player 2 has " + str(player2Score) + " points!")
        elif player1 == player2:
            print("...")
            print("It's a tie!")
            print("...")
            print("Player 1 has " + str(player1Score) + " points!")
            print("Player 2 has " + str(player2Score) + " points!")

        rounds = rounds + 1

    if player1Score > player2Score:
        print("-------------")
        print("***")
        print("Player 1 is the winner!")
        print("***")
    if player1Score < player2Score:
        print("-------------")
        print("***")
        print("Player 2 is the winner!")
        print("***")
    if player1Score == player2Score:
        print("-------------")
        print("***")
        print("It's a draw!! Coincidence?")
        print("***")

def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll



main()
