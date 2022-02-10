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

        White = pygame.image.load('225, 227, 231.png')
        White = pygame.transform.scale(White, (250, 250))
        image = White   
        self.window.blit(image, (200, 70))

        for item in self.roster.buttons_list:

            item.draw(window = self.window)
            pygame.display.update()
        
       

      
    