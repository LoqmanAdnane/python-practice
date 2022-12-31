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
options = [1,2,3,4,5,6,7,8,9]
choice = 0
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
def UserChoice():
    choice = input('Please enter a value corresponding to the available spots in the chart to place your mark (1-9): ')
    return(choice)
while turn < 10:
    if playerTurn == 1:
        print(display(row1, string1, sep1, row2, string2, sep2, row3, string3))
        print('Player 1:')
        UserChoice()
        print(choice)
        print(display(row1, string1, sep1, row2, string2, sep2, row3, string3))
        playerTurn += 1
        turn += 1
    if playerTurn == 2:
        print(display(row1, string1, sep1, row2, string2, sep2, row3, string3))
        print('Player 2:')
        UserChoice()
        print(display(row1, string1, sep1, row2, string2, sep2, row3, string3))
        playerTurn -= 1
        turn += 1