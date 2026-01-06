import pygame

TILE_WIDTH = 50
TILE_HEIGHT = 50
BORDER_WIDTH = 2
class Tile:
    def __init__(self):
        self.containsMine = False
        self.flagged = False
        self.revealed = False
        self.neighbouringMines = 0 # by default
        
    def draw(self, surface, x, y):
        font = pygame.font.SysFont("Ariel", 48)
        
        colour = (0,0,0)
        tile_text = ""

        if self.revealed:
            if self.containsMine:
                colour = (255,255,0)
                tile_text = "*"
            elif self.neighbouringMines>0:
                colour = (0,100,255)
                tile_text = str(self.neighbouringMines)
                if self.neighbouringMines == 1: colour = (0,0,255)
                elif self.neighbouringMines == 2: colour = (0,255,0)
                elif self.neighbouringMines == 3: colour = (255,0,0)
            else:
                colour = (100,100,100)
        else:
            if self.flagged:
                colour = (255,100,0)
                tile_text = "F"
            else:
                colour = (200,200,200)

        #note by colour first then figure out text and images
        pygame.draw.rect(surface, colour,(x+BORDER_WIDTH,y+BORDER_WIDTH,TILE_WIDTH-BORDER_WIDTH*2,TILE_HEIGHT-BORDER_WIDTH*2))
        text_surf = font.render(tile_text,False, (255, 255, 255))
        surface.blit(text_surf,(x+TILE_WIDTH/4,y+TILE_HEIGHT/4))