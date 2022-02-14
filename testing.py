import pygame
from pygame import mixer

pygame.init()

GAME_FONT = pygame.font.SysFont("arial.tff", 24, bold=False, italic=False)

class button:
    def __init__(self, x, y, width, height, color, command): #word
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = command
        #self.word = word
    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))#, self.word)
        #pygame.word.rect()
    def click(self, mousex, mousey):
        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
        return False
    def text(self):
        pass

WIDTH = 500
HEIGHT = 400

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

window = pygame.display.set_mode((WIDTH, HEIGHT))

f = open('song_list.txt')
for element in f:
    titles = element.split(';')
    #for titles in element:
    #text_surface = GAME_FONT.render(titles[0], True, (0, 0, 0))
    #window.blit(text_surface, (200, 200))
    print(titles[0])

gurenge_button = button(50,25,100,50, (100, 232, 159), "demon")
sweater_weather_button = button(50, 100, 100, 50, (108, 109, 112), "sweater")
riptide_button = button(50, 175, 100, 50, (157, 12, 12), "riptide")
worth_it_button = button(50, 250, 100, 50, (233, 169, 49), "worth")
pause_button = button(175, 325, 50, 50, red, "pause")
unpause_button = button(275, 325, 50, 50, blue, "unpause")

SweaterImg = pygame.image.load('Sweater Weather Cover.jpg')

drawable = [gurenge_button, sweater_weather_button, riptide_button, worth_it_button, pause_button, unpause_button]
buttons = [gurenge_button, sweater_weather_button, riptide_button, worth_it_button, pause_button, unpause_button]

run = True

pygame.display.set_caption('Welcome to The Jukebox')

def draw():
    window.fill((225, 227, 231))
    for item in drawable:
        item.draw()
        text_surface = GAME_FONT.render("Jukebox", True, (0, 0, 0))
        window.blit(text_surface, (218, 4))
    pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            for item in buttons:
                if item.click(mousepos[0], mousepos[1]):
                    if item.command == "demon":
                        mixer.init()
                        mixer.music.load("Gurenge (TV Version).wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                    elif item.command == "sweater":
                        mixer.init()
                        #window.fill(green)
                        #window.blit(SweaterImg,(WIDTH/2, HEIGHT/2))
                        pygame.display.flip()
                        mixer.music.load("Sweater Weather.wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                        #pygame.image.load(r'C:Sweater Weather Cover.jpg', (300, 100))
                        #while True:
                            #window.fill(green)
                            #window.blit(SweaterImg,(0,0))                        
                    elif item.command == "riptide":
                        mixer.init()
                        mixer.music.load("Riptide.wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                    elif item.command == "worth":
                        mixer.init()
                        mixer.music.load("Worth It.wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                    if item.command == "pause":
                        pygame.mixer.music.pause()
                    if item.command == "unpause":
                        pygame.mixer.music.unpause()
    draw()
    

    
    
pygame.quit()