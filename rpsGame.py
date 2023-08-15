import sys,random

print("ROCK,PAPER,SCISSORS")

#To keep track of the score
wins = 0
losses = 0
ties = 0

while True:                         #This is the main game loop
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter Your Move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()             #Quit the game/program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break                  #To break out of player input loop
        print('Type one of r, p, s or q')

    #Display What The Player Chose:
    if playerMove == 'r':
        print('ROCK versus ......')
    elif playerMove == 'p':
        print('PAPER versus ......')
    elif playerMove == 's':
        print('SCISSORS versus ......')

    #Display What The Computer Chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    #Display and Record Win/Loss/Tie:
    if playerMove == computerMove:
        print('It is a Tie!!!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win!!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win!!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You Loss!!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You Loss!!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You Loss!!')
        losses = losses + 1
