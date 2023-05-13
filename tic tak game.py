import random
from replit import clear

# I made a 2D array to display grid
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# I made another 2D array to hold the positions
positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# counts the no. of entries
count = 0


# display the Grid
def diplay_grid():
    print(f"\n_________________")
    for i in range(0, 3):
        for j in range(0, 3):
            print(f"| {grid[i][j]} |", end=' ')
        print(f"\n_________________")


# check for the result
def check_results():
    won = False
    global count, grid
    for i in range(0, 3):
        # all rows
        if grid[0][i] == grid[1][i] == grid[2][i]:
            won = True
            winner = grid[0][i]
        # all columns
        if grid[i][0] == grid[i][1] == grid[i][2]:
            won = True
            winner = grid[i][0]

    # left diagonal
    if grid[0][0] == grid[1][1] == grid[2][2]:
        won = True
        winner = grid[0][0]

    # right diagonal
    if grid[0][2] == grid[1][1] == grid[2][0]:
        won = True
        winner = grid[0][2]

    # if anyone wins display the result
    if won:
        print(f"{winner} WON!!!!")
        print(f"Let's restart the game")
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        count = 0
        input()
        clear()


# Adds X or O to the grid
def add_num(position):
    global count
    for i in range(0, 3):
        for j in range(0, 3):
            # checking the position
            if positions[i][j] == position:
                # if that position is not taken fill it
                if grid[i][j] != "X" and grid[i][j] != "O":
                    grid[i][j] = player
                    count += 1
                    return True
                else:
                    # display message for the user and take another position
                    print(f"{positions[i][j]}   {position}")
                    if player == "X":
                        print("Position already taken! ")
                        position = input("Enter your position: ")
                        position = int(position)
                    else:
                        # regenerate the position for computer
                        position = random.randint(1, 9)

    return False


x = True
player = 'X'
print("Lets start Tic Tac Toe Game! ")
print("**************************************")
print("You are X and computer is O:")
print("**************************************")

while count < 9:
    # display grid each time
    diplay_grid()
    if player == 'X' and x == True:
        # Get the position for X
        position = input("Enter your position: ")
        position = int(position)
    else:
        # regenerate the position for computer
        position = random.randint(1, 9)

    # add to the position
    if add_num(position):
        # switch the player
        if player == "X":
            player = "O"
            x = False
        else:
            player = "X"
            x = True

    check_results()
