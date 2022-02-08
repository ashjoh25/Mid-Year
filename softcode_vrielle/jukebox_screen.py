import pygame 

class Screen (object):

    def __init__ (self, window, roster):
        
        self.GAME_FONT = pygame.font.SysFont("arial.tff", 24, bold = False, italic = False)

        self.window = window
        pygame.display.set_caption('Welcome to The Jukebox')
        self.window.fill((225, 227, 231))
        self.roster = roster

        self.create_widgets()

    def create_widgets(self):
        
        text_surface = self.GAME_FONT.render("Jukebox", True, (0, 0, 0))
        self.window.blit(text_surface, (218, 4))

        for item in self.roster:

            item.draw()
            pygame.display.update()

      
    