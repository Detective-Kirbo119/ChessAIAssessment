import pygame 
import sys

from const import *
from game import Game



class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        ##self.clock = pygame.time.Clock()self.running = True
        self.game = Game()
        
        
    def mainloop(self):

        screen = self.screen    
        game = self.game

        while True:
            game.show_bg(self.screen)
            game.show_pieces(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()

main = Main()
main.mainloop()

