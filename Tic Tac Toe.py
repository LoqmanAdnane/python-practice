sep1 = '_____'
sep2 = '_____'
row1 = ['1','|','2','|','3']
row2 = ['4','|','5','|','6']
row3 = ['7','|','8','|','9']
string1 = ''
string2 = ''
string3 = ''
playerTurn = 1
turn = 0
options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
choice = 'empty'
def display(row1, string1, sep1, row2, string2, sep2, row3, string3):
    for x in row1:
        string1 += x
    for x in row2:
        string2 += x
    for x in row3:
        string3 += x
    print(string1)
    print(sep1)
    print(string2)
    print(sep2)
    print(string3)
def userChoice(choice):
    while choice.isdigit() == False and choice not in options:
        choice = input('Please enter a value corresponding to the available spots in the chart to place your mark (1-9): ')
        if choice.isdigit() == False:
            print("Sorry that is not a digit. Please enter a number from 1-9.")
        elif choice not in options:
            print("Sorry that place was used already, select one of the following digits")
        else:
            return(choice)
def boardUpdate(choice):
    if playerTurn == 1:
        for x in row1:
            if x == choice:
                x = 'X'
        for x in row2:
            if x == choice:
                x = 'X'
        for x in row3:
            if x == choice:
                x = 'X'
    else:
        for x in row1:
            if x == choice:
                x = 'O'
        for x in row2:
            if x == choice:
                x = 'O'
        for x in row3:
            if x == choice:
                x = 'O'
while turn < 10:
    if playerTurn == 1:
        display(row1, string1, sep1, row2, string2, sep2, row3, string3)
        print('Player 1:')
        userChoice(choice)
        boardUpdate(choice)
        print(choice)
        display(row1, string1, sep1, row2, string2, sep2, row3, string3)
        playerTurn += 1
        turn += 1
    if playerTurn == 2:
        display(row1, string1, sep1, row2, string2, sep2, row3, string3)
        print('Player 2:')
        userChoice(choice)
        boardUpdate(choice)
        display(row1, string1, sep1, row2, string2, sep2, row3, string3)
        playerTurn -= 1
        turn += 1
if playerTurn == 10:
    print('Fin')
    ##Construct system for calculating winner perhaps by using rows = x or o