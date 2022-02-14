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
        
        #mixer.music.load(str(roster[command].music))
        text_surface = self.GAME_FONT.render("Jukebox", True, (0, 0, 0))
        self.window.blit(text_surface, (218, 4))

        White = pygame.image.load('225, 227, 231.png')
        White = pygame.transform.scale(White, (250, 250))
        image = White   
        self.window.blit(image, (200, 70))

        for item in self.roster.buttons_list:

            item.draw(window = self.window)
            pygame.display.update()
        
       

        self.window.blit(play, (275, 325))
        self.window.blit(pause, (175, 325))

    #def play_pause(self, x, y, width, height, color, command):

        
        #self.x = x
        #self.y = y
        #self.width = width
        #self.height = height
        #self.color = color
        #self.command = command
        #play_button = Button(175, 325, 50, 50, (255, 255, 255), "play")
        #pause_button = Button(275, 325, 50, 50, (255, 255, 255), "pause")
        #play = pygame.image.load('Play Button Icon.png')
        #play = pygame.transform.scale(play, (50, 50))
        #pause = pygame.image.load('Pause Button Icon.png')
        #pause = pygame.transform.scale(pause, (50, 50))

        #drawable = [play_button, pause_button]

        #for item in drawable:
            #item.draw()
            #self.window.blit(play, (275, 325))
            #self.window.blit(pause, (175, 325))

      
    