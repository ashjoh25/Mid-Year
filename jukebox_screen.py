import pygame 
from button_object import StandardButton, PlayPauseButton

class SongScreen (object):

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

        play_img = pygame.image.load('Play Button Icon.png')
        play_img = pygame.transform.scale(play_img, (50, 50))
        pause_img = pygame.image.load('Pause Button Icon.png')
        pause_img = pygame.transform.scale(pause_img, (50, 50))
        
        pause_button = StandardButton(175, 325, 50, 50, (225, 227, 231), "pause", text = None)
        unpause_button = StandardButton(275, 325, 50, 50, (225, 227, 231), "unpause", text = None)

        pause_button = PlayPauseButton(pause_button)
        unpause_button = PlayPauseButton(unpause_button)

        self.roster.song_buttons_list.append(pause_button)
        self.roster.song_buttons_list.append(unpause_button)

        for item in self.roster.song_buttons_list:

            item.standard_button.draw(window = self.window)
            self.window.blit(play_img, (275, 325))
            self.window.blit(pause_img, (175, 325))
            pygame.display.update()
        

      
    