import pygame
from pygame import mixer
from pygame.locals import *

pygame.init()

font = pygame.font.SysFont('Arial', 30)

#define colours
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

clicked = False
counter = 0
class button:
    #colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, text, width, height, color, command): #word
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.color = color
        self.command = command
        #self.word = word

    def draw_button(self):

        global clicked
        action = False

        pos = pygame.mouse.get_pos()

        button_rect = Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(window, self.click_col, button_rect)  
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(window, self.hover_col, button_rect)
        else:
            pygame.draw.rect(window, self.button_col, button_rect)
		
		#add shading to button
        pygame.draw.line(window, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(window, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(window, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(window, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        window.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

WIDTH = 500
HEIGHT = 400

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

window = pygame.display.set_mode((WIDTH, HEIGHT))

# IGNORE FOR NOW
# f = open('song_list.txt')
# for element in f:
    # titles = element.split(';')
    #for titles in element:
    #text_surface = GAME_FONT.render(titles[0], True, (0, 0, 0))
    #window.blit(text_surface, (200, 200))
    # print(titles[0])

# (self, x, y, width, height, color, command)
gurenge = button(75, 200, 'Gurenge')
sweater_weather = button(325, 200, 'Sweater Weather')
riptide = button(75, 350, 'Riptide')
worth_it = button(325, 350, 'Worth It')

pause_button = button(175, 325, 50, 50, red, "pause")
unpause_button = button(275, 325, 50, 50, blue, "unpause")

Sweater_Img = pygame.image.load('Sweater Weather Cover.jpg')

run = True

pygame.display.set_caption('Welcome to The Jukebox')

def draw():
    window.fill((225, 227, 231))
    if again.draw_button():
        print('Gurenge')
        counter = 0
        if quit.draw_button():
            print('Sweater Weather')
        if up.draw_button():
		print('Riptide')
		counter += 1
	if down.draw_button():
		print('Worth It')
		counter -= 1
    pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            for item in buttons:
                # if item.click(mousepos[0], mousepos[1]):
                    # if item.command == "demon":
                    #     mixer.init()
                    #     mixer.music.load("Gurenge (TV Version).wav")
                    #     mixer.music.set_volume(0.7)
                    #     mixer.music.play()
                    if item.command == "sweater":
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
