import pygame

from button_object import Button, Button_Roster
from jukebox_screen import Screen


class Jukebox_Manager(object):

    def __init__(self):
        
        self.window = None
        self.current_screen = None
        self.roster = None
        self.run = True

        pygame.init()

    def setup_screen(self):
        
        self.window = pygame.display.set_mode((500, 400))
        self.roster = Button_Roster("jukebox_songs.txt")
        self.current_screen = Screen(window = self.window, roster = self.roster)


    def loop(self):

        while self.run == True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run == False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    
                    for item in self.roster:
                        
                        if item.click(mousepos[0], mousepos[1]) and item.command >= 0:
                            
                            item.play(command = self.command, roster = self.roster)
            
        pygame.quit()

def main():

    jukebox = Jukebox_Manager()
    jukebox.setup_screen()

main()
    
