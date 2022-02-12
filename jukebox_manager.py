import pygame

from button_object import SongButtonRoster
from jukebox_screen import SongScreen

class Jukebox_Manager (object):

    def __init__(self):
        
        self.window = pygame.display.set_mode((500, 400))
        self.current_screen = None
        self.roster = None
        self.run = True

    def setup_song_screen(self):
        
        pygame.display.set_caption('Welcome to The Jukebox!')
        self.roster = SongButtonRoster ("song_list.txt")
        self.current_screen = SongScreen (window = self.window, roster = self.roster)


    def loop(self):
        
        self.setup_song_screen()

        while self.run == True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    
                    for item in self.roster.song_buttons_list:
                        
                        if item.standard_button.click(mousepos[0], mousepos[1]):
                        
                            if len(item.standard_button.command) == 1:
                            
                                item.play(command = int(item.standard_button.command), roster = self.roster.song_buttons_list)
                                item.place_image(command = int(item.standard_button.command), roster = self.roster.song_buttons_list, window = self.window)
                            
                            elif item.standard_button.command == "pause":
                                item.pause()

                            elif item.standard_button.command == "unpause":
                                item.unpause()
                                
def main():

    pygame.init()
    jukebox = Jukebox_Manager()
    jukebox.loop()

main()
