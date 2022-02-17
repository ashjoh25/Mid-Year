import pygame
from button_object import StandardButton

class GenreScreen (object):

    def __init__(self, window, roster, callback_on_selected):

        self.GAME_FONT = pygame.font.SysFont("arial.tff", 24, bold = False, italic = False)

        self.window = window
        self.callback_on_selected = callback_on_selected
        self.roster = roster 
        self.run = True

        self.create_widgets()
        self.loop()

    def create_widgets(self):

        pygame.display.set_caption('Welcome to the Jukebox!')
        self.window.fill((225, 227, 231))
        
        text_surface = self.GAME_FONT.render("Genres", True, (0, 0, 0))
        self.window.blit(text_surface, (218, 10))

        for item in self.roster.genre_buttons_list:

            item.standard_button.draw(window = self.window)
        
        pygame.display.update()
        
    def loop (self):
        
        while self.run == True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    
                    for item in self.roster.genre_buttons_list:
                        
                        if item.standard_button.click(mousepos[0], mousepos[1]):
                        
                            self.callback_on_selected(item.file_name, item.color_theme, item.standard_button.txt)
                            self.run = False
