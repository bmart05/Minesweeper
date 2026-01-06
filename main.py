from grid import Grid, rowNum
import pygame

width = 8
height = 8
noMines = 10

# while True:

#     difficulty = input("Welcome to Minesweeper! What difficulty would you like: easy(8x8), medium(16x16), hard(30x16), impossible(36x36) ")

#     if difficulty == "easy":
#         width = 8
#         height = 8
#         noMines = 10
#         break
#     elif difficulty == "medium":
#         width = 16
#         height = 16
#         noMines = 40
#         break
#     elif difficulty == "hard":
#         width = 30
#         height = 16
#         noMines = 99
#         break
#     elif difficulty == "impossible":
#         width = 36
#         height = 36
#         noMines = 260
#         break
#     else:
#         print("Invalid difficulty, pick again")

pygame.init()
screen = pygame.display.set_mode((800,800))

totalMoves = 0
grid = Grid(width,height,noMines)


running = True

while running:\

    finished = grid.checkFinished() # checks to see if all tiles are revealed and all mines are flagged
    if finished:
        print(f"Congratulations, you got all the mines in {totalMoves} moves!")
        running = False
        continue


    #rendering
    screen.fill((0,0,255))

    pygame.display.flip()

    # command = input("Type f{x,y} for flag or c{x,y} to check").upper()
    # x = rowNum.find(command[1])
    # y = rowNum.find(command[2])
    # print(f"{x}:{y}")
    # if command[0] == 'C':
    #     if totalMoves == 0:
    #         safeMove = False
    #         while not safeMove: # regenerate all mines if the move contains a mine, do this until they don't
    #             grid.setup()
    #             safeMove = not (grid.grid[x][y].containsMine or grid.grid[x][y].neighbouringMines > 0) # not a safe move if it contains a mine

    #     containsMine = grid.checkTile(x,y)
    #     if containsMine:
    #         print("You hit a mine. Game over!")
    #         grid.gameOver()
    #         running = False
    # elif command[0] == 'F':
    #     grid.toggleFlag(x,y)
    # else:
    #     print("Invalid command")
    totalMoves+=1



