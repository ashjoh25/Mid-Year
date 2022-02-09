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
            c += 1
            # say if button added or +1 in button counter, change the color
            # make each number (x, u, z) a variable that will then change or get subtracted
            x = 240
            u = 125
            z = 255
            newButtonColor = (int(x), int(y), int(z))
            if c + 1:
                x -= 30
                u -= 30
                z -= 30
                newButtonColor = (int(x), int(y), int(z))

            line = line.strip()
            line_elements = line.split(';')
            b = Button(50, y, 100, 50, newButtonColor, index, line_elements[0], line_elements[1])
            self.buttons_list.append(b)

            y += 75 
            index += 1

