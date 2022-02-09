import pygame

from button_object import ButtonRoster
from jukebox_screen import Screen

class Jukebox_Manager (object):

    def __init__(self):
        
        self.window = pygame.display.set_mode((500, 400))
        self.current_screen = None
        self.roster = None
        self.run = True

    def setup_screen(self):
        
        pygame.display.set_caption('Welcome to The Jukebox!')
        self.roster = ButtonRoster ("song_list.txt")
        self.current_screen = Screen (window = self.window, roster = self.roster)


    def loop(self):
        
        self.setup_screen()

        while self.run == True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    
                    for item in self.roster.buttons_list:
                        
                        if item.click(mousepos[0], mousepos[1]) and item.command >= 0:
                            
                            item.play(command = item.command, roster = self.roster.buttons_list)
                            item.place_image(command = item.command, roster = self.roster.buttons_list, window = self.window)
                            
            pygame.display.update()

def main():

    pygame.init()
    jukebox = Jukebox_Manager()
    jukebox.loop()

main()
    
