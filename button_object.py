import pygame
from pygame import mixer

class StandardButton (object):

    def __init__(self, x, y, width, height, color, index): 

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = index

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))#, self.word)

    def click(self, mousex, mousey):

        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
            
        return False

    def button_text(self):
        pass

class SongButton (object):

    def __init__(self, button, music, image, text):

        self.standard_button = button
        self.music = music
        self.image = image
        self.text = text

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


class SongButtonRoster (object):

    def __init__(self, file_name):

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
            b = StandardButton(50, y, 100, 50, newButtonColor, str(index))
            b = SongButton(button = b, music = line_elements[1], image = line_elements[2], text = line_elements[0])
            self.song_buttons_list.append(b)

            y += 75 
            index += 1

