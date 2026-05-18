#importing random for bot random choice
import random

#optimize the input expectation to preven crashes
while True:
    try:
        player_picked=int(input("[1]: Rock \n[2]: Paper \n[3]: scissors \nPicked(number only): ")) #I used 1,2 and 3 inputs expection to make easier for user to choose and lest type for them
    
        if 1<= player_picked <=3:
            break
        else: print("Input upto 1,2 and 3 only. Pls try again")
    except:
        print("Input error. Pls try again")

option= ["rock", "paper", "scissors"]

player= option[player_picked-1]
bot = random.choice(option)

#function of game logic
def start(player, bot):
    win_scenarios={"rock": "scissors", "paper": "rock", "scissors": "paper"}
    print(
    "YOU choose: ", player, "\n"
    "BOT choose: ", bot , "\n"
    )

    #easiest and shortest logic i can think of to make my code more efficient and not repeatable used of if/elif
    if player == bot:
        print("DRAW! Bot choose", bot, " too!")
    elif win_scenarios[player] == bot:
        print("You won! :)")
    else: print("You Lose :(")

#calling the fucntion to start the game
start(player, bot)
