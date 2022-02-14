import pygame
from pygame import mixer

class Button (object):

    def __init__(self, x, y, width, height, color, index, text, music): 

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = index
        self.text = text
        self.music = music

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))#, self.word)

    def click(self, mousex, mousey):

        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
        return False

    def play(self, command, roster):

        pygame.mixer.init()
        mixer.music.load(str(roster[command].music))
        mixer.music.set_volume(0.7)
        mixer.music.play()

    def button_text(self, text):
        pass

class ButtonRoster (object):

    def __init__(self, file_name):

        self.buttons_list = []
        y = 25
        c = 0
        index = 0 
        f = open(file_name)

        for line in f:
            line = line.strip()
            line_elements = line.split(';')
            b = Button(50, y, 100, 50, (c, c, c), index, line_elements[0], line_elements[1])
            self.buttons_list.append(b)

            y += 75 
            c += 30 
            index += 1