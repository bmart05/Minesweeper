import random
from tile import Tile
from colorama import Fore, Style, Back

checkingGrid = [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
class Grid:
    def __init__(self,width,height,mines):
        self.width = width
        self.height = height
        self.noMines = mines
        self.grid = []

        self.setup() 


    def setup(self):
        # initialize grid
        self.grid = [] # clear grid if resetting
        for y in range(self.height):
            row = []
            for x in range(self.width):
                tile = Tile()
                tile.revealed = False
                row.append(tile)
            self.grid.append(row)

        # place mines
        minesPlaced = 0
        while minesPlaced < self.noMines:
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            tile = self.grid[x][y]
            tile.containsMine = True
            minesPlaced += 1

        # calculate neighbouring bombs
        for y in range(self.height):
            for x in range(self.width):
                tile = self.grid[x][y]
                tile.neighbouringMines = self.calculateNeighbouringMines(x,y)

    def checkFinished(self):
        total = 0
        for y in range(self.height):
            for x in range(self.width):
                tile = self.grid[x][y]
                if tile.revealed:
                    total += 1
                if tile.flagged and tile.containsMine:
                    total +=1
        if total == (self.width*self.height): # all tiles
            return True
        else:
            return False
        
    def gameOver(self):
        print(f'{Fore.BLACK}{Back.WHITE}  ' + ' '.join([str(x) for x in range(self.width)])+f'  {Style.RESET_ALL}')
        for y in range(self.height):
            row = f"{Fore.BLACK}{Back.WHITE}{str(y)}{Style.RESET_ALL} "
            for x in range(self.width):
                tile = self.grid[x][y]
                tile.revealed = True
                row += tile.draw() + " "
            print(row + f"{Fore.BLACK}{Back.WHITE} {Style.RESET_ALL} ")

    def calculateNeighbouringMines(self,x,y):
        # check [x,y+1],[x+1,y+1],[x+1,y],[x+1,y-1],[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1]

        noMines = 0
        for neighbour in checkingGrid:
            nx =x + neighbour[0]
            ny = y + neighbour[1]
            if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                continue
            if x == nx and y == ny:
                continue
            if self.grid[nx][ny].containsMine: 
                noMines+=1
        return noMines

    def toggleFlag(self,x,y):
        tile = self.grid[x][y]
        tile.flagged = not tile.flagged

    def checkTile(self,x,y):
        # run flood fill algorithm
        tile = self.grid[x][y]
        if tile.containsMine:
            # game ends
            tile.revealed = True
            return True
        else:
            self.floodFill(x,y)
            return False
    def floodFill(self,x,y):
        tile = self.grid[x][y]
        if tile.neighbouringMines == 0:
            tile.revealed = True
            for neighbour in checkingGrid:
                nx = x + neighbour[0]
                ny = y + neighbour[1]
                if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                    continue

                neighbourTile = self.grid[nx][ny]
                if not neighbourTile.revealed:
                    self.floodFill(nx,ny)
        elif not tile.containsMine: # must be a number tile if it has neighbours and it is not a  mine
            tile.revealed = True         
        else:
            return