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

#    def play_pause(self, x, y, width, height, color, command):
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#        self.color = color
#        self.command = command
#        play_button = Button (175, 325, 50, 50, (255, 255, 255), mixer.music.play())
#        pause_button = Button(275, 325, 50, 50, (255, 255, 255), mixer.music.pause())
#        play = pygame.image.load('Play Button Icon.png')
#        play = pygame.transform.scale(play, (50, 50))
#        pause = pygame.image.load('Pause Button Icon.png')
#        pause = pygame.transform.scale(pause, (50, 50))

    def button_text(self, text):
        pass

class pausePlaybutton(object):

    def __init__(self, x, y, width, height, color, command) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = command
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))#, self.word)

    def click(self, mousex, mousey):

        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
        return False

    #def playPause(self):
        
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
            x = 231
            u = 0
            z = 255

            if c + 1:
                x += 10
                u += 20
                newButtonColor = (int(x), int(y), int(z))

            line = line.strip()
            line_elements = line.split(';')
            b = Button(50, y, 100, 50, newButtonColor, index, line_elements[0], line_elements[1])
            self.buttons_list.append(b)

            y += 75 
            index += 1

