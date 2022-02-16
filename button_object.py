from curses import window
import pygame
from pygame import mixer
from pygame.locals import *

pygame.init()


font = pygame.font.SysFont("Arial", 30)

#define colours
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
counter = 0
class StandardButton (object):

    	#colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255) 
    click_col = (50, 150, 255)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, txt, width, height, color, index,): 

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = index
        self.txt = txt

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))#, self.word)

    def click(self, mousex, mousey):

        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
            
        return False
    
    def draw_line(self):
        pygame.draw.line(window, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(window, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(window, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(window, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

class SongButton (object):

    def __init__(self, button, music, image):

        self.standard_button = button
        self.music = music
        self.image = image

    def play(self, command, roster):

        pygame.mixer.init()
        mixer.music.load(str(roster[command].music))
        mixer.music.set_volume(0.7)
        mixer.music.play()
    
    def place_image(self, command, roster, window):

        image = pygame.image.load(str(roster[command].image))
        image = pygame.transform.scale(image, (250,250))
        window.blit(image, (200, 51))
        pygame.display.update()

class PlayPauseButton (object):

    def __init__(self, button):

        self.standard_button = button 

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

class GenreButton (object):

    def __init__(self, button, file_name):

        self.standard_button = button 
        self.file_name = file_name

class SongButtonRoster (object):

    def __init__(self, file_name): # color (t, u, z)

        self.song_buttons_list = []
        y = 25
        c = 0
        index = 0 
        f = open(file_name)

        for line in f:
            c += 1

            # say if button added or +1 in button counter, change the color
            # make each number (x, u, z) a variable that will then change or get subtracted
            x = 231
            u = 0
            z = 255

            if c + 1:
                x += 10
                u += 20
                newButtonColor = (int(x), int(y), int(z))

            line = line.strip()
            line_elements = line.split(';')
            b = StandardButton(50, y, 100, 50, newButtonColor, str(index), line_elements[0])
            b = SongButton(button = b, music = line_elements[1], image = line_elements[2])
            self.song_buttons_list.append(b)

            y += 75 
            index += 1

class GenreButtonRoster (object):

    def __init__(self, file_name):

        self.genre_buttons_list = []
        x = 20
        y = 25
        c = 0
        index = 0 
        f = open(file_name)

        for line in f:
            c += 1

            # say if button added or +1 in button counter, change the color
            # make each number (x, u, z) a variable that will then change or get subtracted
            t = 231
            u = 0
            z = 255

            if c + 1:
                t += 10
                u += 20
                newButtonColor = (int(t), int(y), int(z))

            line = line.strip()
            line_elements = line.split(';')

            b = StandardButton(x, 240, 100, 100, newButtonColor, str(index), line_elements[0])
            b = GenreButton(b, line_elements[1])

            self.genre_buttons_list.append(b)

            x += 120
            index += 1

