from random import randint

# colors
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
M = '\033[35m'  # magenta

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
    raise SystemExit(R + 'Oops, invalid input! Please try again ...')

# getting computer's input
computer_random_number = randint(1, 3)
computers_turn = ''
if computer_random_number == 1:
    computers_turn = rock
elif computer_random_number == 2:
    computers_turn = paper
elif computer_random_number == 3:
    computers_turn = scissors
print(B + f'The computer chose {computers_turn}!')

# comparing the results
if (players_turn == rock and computers_turn == scissors) or \
        (players_turn == paper and computers_turn == rock) or \
        (players_turn == scissors and computers_turn == paper):
    print(O + 'Congratulations! You won!!!')
elif players_turn == computers_turn:
    print(M + 'Draw')
else:
    print(P + 'Sorry, you lost!')
