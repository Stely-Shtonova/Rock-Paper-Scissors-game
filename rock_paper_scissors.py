from random import randint

# colors
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
M = '\033[35m'  # magenta

your_wins = 0
computers_wins = 0
while True:
    # getting user's input
    players_turn = input(G + "It's your turn! Click [r] for rock, [p] for paper or [s] for scissors:\n")
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    if players_turn.lower() == 'r':
        players_turn = rock
    elif players_turn.lower() == 'p':
        players_turn = paper
    elif players_turn.lower() == 's':
        players_turn = scissors
    else:
        print(R + 'Oops, invalid input! Please try again ...')
        continue
    # getting computer's input
    computer_random_number = randint(1, 3)
    computers_turn = ''
    if computer_random_number == 1:
        computers_turn = rock
    elif computer_random_number == 2:
        computers_turn = paper
    elif computer_random_number == 3:
        computers_turn = scissors
    print(B + f'The computer chose {computers_turn.title()}!')
    # comparing results and calculating wins
    if (players_turn == rock and computers_turn == scissors) or \
            (players_turn == paper and computers_turn == rock) or \
            (players_turn == scissors and computers_turn == paper):
        print(O + 'Congratulations! You won!!!')
        your_wins += 1
    elif players_turn == computers_turn:
        print(M + 'Draw')
    else:
        print(P + 'Sorry, you lost!')
        computers_wins += 1
    # prompting the user to play again
    print()
    go_again = False
    while True:
        answer = input(P + 'Would you like to play again? Write either [yes] or [no] below:\n')
        if answer.lower() == 'yes':
            go_again = True
            break
        elif answer.lower() == 'no':
            if your_wins > computers_wins:
                message = f"Thanks for playing! Here's the final score: {your_wins}:{computers_wins} for You"
            elif your_wins == computers_wins:
                message = f"Thanks for playing! Here's the final score: {your_wins}:{computers_wins} You both played well!"
            else:
                message = f"Thanks for playing! Here's the final score: {your_wins}:{computers_wins} for The computer"
            print(O + message)
            raise SystemExit
        else:
            print(R + 'Please enter a valid input!')
            continue
