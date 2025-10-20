from grid import Grid
from colorama import Fore,Back,Style

width = 8
height = 8
noMines = 10
totalMoves = 0
grid = Grid(width,height,noMines)

running = True

while running:
    print(f'{Fore.BLACK}{Back.WHITE}  ' + ' '.join([str(x) for x in range(width)])+f'{Style.RESET_ALL}')
    for y in range(grid.height):
        row = f"{Fore.BLACK}{Back.WHITE}{str(y)}{Style.RESET_ALL} "
        for x in range(grid.width):
            tile = grid.grid[x][y]
            row += tile.draw() + " "
        print(row)

    finished = grid.checkFinished()
    if finished:
        print("Congratulations, you got all the mines!")
        running = False
        continue

    command = input("Type f{x,y} for flag or c{x,y} to check")
    x = int(command[1])
    y = int(command[2])
    if command[0] == 'c':

        containsMine = grid.checkTile(x,y)
        if containsMine:
            # if totalMoves == 0:
            #     safeMove = False
            #     while not safeMove: # regenerate all mines if the move contains a mine, do this until they don't
            #         grid.setup()
            #         safeMove = not grid.grid[x][y].containsMine # not a safe move if it contains a mine
            # else:
            print("You hit a mine. Game over!")
            grid.gameOver()
            running = False
    elif command[0] == 'f':
        grid.toggleFlag(x,y)
    else:
        print("Invalid command")
    totalMoves+=1



