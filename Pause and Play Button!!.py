import pygame
from pygame import mixer

class button:
    def __init__(self, x, y, width, height, color, command):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = command
    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
    def click(self, mousex, mousey):
        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
        return False

WIDTH = 500
HEIGHT = 400

# make color gradient for buttons
bg_color = (235, 224, 245)
# keeping these for hard code
bc1 = (147, 133, 255)
bc2 = (185, 148, 255)
bc3 = (222, 157, 255)
bc4 = (245, 168, 255)

# say if button added or +1 in button counter, change the color
# make each number (x, y, z) a variable that will then change or get subtracted
# making random counter variable so there is no error for now
counter = 0
x = 240
y = 125
z = 255
newButtonColor = (int(x), int(y), int(z))
if counter + 1:
    x -= 30
    y -= 30
    z -= 30
    newButtonColor = (int(x), int(y), int(z))

# pause and unpause need independent variables because they aren't in the list of songs
unpause_c = (255, 255, 255)
pause_c = (237, 237, 237)


window = pygame.display.set_mode((WIDTH, HEIGHT))

gurenge_button = button(50,25,100,50, (100, 232, 159), "demon")
sweater_weather_button = button(50, 100, 100, 50, (108, 109, 112), "sweater")
riptide_button = button(50, 175, 100, 50, bc1, "riptide")
worth_it_button = button(50, 250, 100, 50, bc2, "worth")
pause_button = button(175, 300, 50, 50, pause_c, "pause")
unpause_button = button(275, 300, 50, 50, unpause_c, "unpause")

drawable = [gurenge_button, sweater_weather_button, riptide_button, worth_it_button, pause_button, unpause_button]
buttons = [gurenge_button, sweater_weather_button, riptide_button, worth_it_button, pause_button, unpause_button]

run = True

pygame.display.set_caption('Welcome to The Jukebox')

def draw():
    window.fill(bg_color)
    for item in drawable:
        item.draw()
    pygame.display.update()

while run:
    for event in pygame.event.get():
        #gameDisplay.fill(white)
        #largeText = pygame.font.Font('freesansbold.ttf',115)
        #TextSurf, TextRect = ("Riptide", largeText)
        #TextRect.center = ((window.width/2),(window.height/2))
        #gameDisplay.blit(TextSurf, TextRect)
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
                        mixer.music.load("Sweater Weather.wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                        #pygame.image.load(r'C:Sweater Weather Cover.jpg', (300, 100))
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
