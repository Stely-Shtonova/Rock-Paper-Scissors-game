from random import randint

# getting user's input
players_turn = input("It's your turn! Click [r] for rock, [p] for paper or [s] for scissors:\n")
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
    raise SystemExit('Oops, invalid input! Please try again ...')

# getting computer's input
computer_random_number = randint(1, 3)
computers_turn = ''
if computer_random_number == 1:
    computers_turn = rock
elif computer_random_number == 2:
    computers_turn = paper
elif computer_random_number == 3:
    computers_turn = scissors
print(f'The computer chose {computers_turn}!')

# comparing the results
if (players_turn == rock and computers_turn == scissors) or \
    (players_turn == paper and computers_turn == rock) or \
    (players_turn == scissors and computers_turn == paper):
    print('Congratulations! You won!!!')
elif players_turn == computers_turn:
    print('Draw')
else:
    print('Sorry, you lost!')
