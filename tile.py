from colorama import Fore, Style, Back

class Tile:
    def __init__(self):
        self.containsMine = False
        self.flagged = False
        self.revealed = False
        self.neighbouringMines = 0 # by default
        
    def draw(self):
        if self.revealed:
            if self.containsMine:
                return f"{Fore.CYAN}*{Style.RESET_ALL}" # red text
            if self.neighbouringMines>0:
                color = Fore.CYAN
                if self.neighbouringMines == 1: color = Fore.BLUE
                elif self.neighbouringMines == 2: color = Fore.GREEN
                elif self.neighbouringMines == 3: color = Fore.RED
                return f"{color}{str(self.neighbouringMines)}{Style.RESET_ALL}"
            else:
                return ' ' # for blank tiles
        else:
            if self.flagged:
                return f"{Fore.WHITE}{Back.RED}F{Style.RESET_ALL}"
            else:
                return '.'
