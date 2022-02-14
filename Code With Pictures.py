import pygame
from pygame import mixer

pygame.init()

all_fonts = pygame.font.get_fonts()

#sweaterImg = pygame.image.load('Sweater Weather Cover.png')


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
        pygame.draw.rect(DISPLAY, self.color, (self.x, self.y, self.width, self.height))#, self.word)
        #pygame.word.rect()
    def click(self, mousex, mousey):
        if self.x <= mousex <= self.x + self.width and self.y <= mousey <= self.y + self.height:
            return True
        return False
    def text(self):
        pass

Gimg = pygame.image.load('Gurenge Cover.jpg')
Gimg = pygame.transform.scale(Gimg, (250,250))
SWimg = pygame.image.load('SweaterWeatherCover.png')
SWimg = pygame.transform.scale(SWimg, (250,250))
Rimg = pygame.image.load('Riptide Cover.jpg')
Rimg = pygame.transform.scale(Rimg, (250,250))
WIimg = pygame.image.load('Worth It Album.png')
WIimg = pygame.transform.scale(WIimg, (250,250))
White = pygame.image.load('225, 227, 231.png')
White = pygame.transform.scale(White, (250, 250))
image = White

WIDTH = 500
HEIGHT = 400

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

f = open('song_list.txt')
for element in f:
    titles = element.split(';')
    #for titles in element:
    #text_surface = GAME_FONT.render(titles[0], True, (0, 0, 0))
    #window.blit(text_surface, (200, 200))
    print(titles[0])

bc1 = (147, 133, 255)
bc2 = (185, 148, 255)
bc3 = (222, 157, 255)
bc4 = (245, 168, 255)
unpause_c = (225, 227, 231)
pause_c = (225, 227, 231)

gurenge_button = button(50,25,100,50, bc1, "demon")
sweater_weather_button = button(50, 100, 100, 50, bc2, "sweater")
riptide_button = button(50, 175, 100, 50, bc3, "riptide")
worth_it_button = button(50, 250, 100, 50, bc4, "worth")
pause_button = button(175, 325, 50, 50, pause_c, "pause")
unpause_button = button(275, 325, 50, 50, unpause_c, "unpause")

drawable = [gurenge_button, sweater_weather_button, riptide_button, worth_it_button, pause_button, unpause_button]
buttons = [gurenge_button, sweater_weather_button, riptide_button, worth_it_button, pause_button, unpause_button]

run = True

pygame.display.set_caption('Welcome to The Jukebox')
def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
    
_cached_fonts = {}
def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

_cached_text = {}
def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image

pygame.init()
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
done = False

font_preferences = [
        "Comic Sans",
        "Arial",
        "Papyrus",
        "Comic Sans MS"]

text = create_text("Jukebox", font_preferences, 50, (0, 128, 0))

play = pygame.image.load('Play Button Icon.png')
play = pygame.transform.scale(play, (50, 50))
pause = pygame.image.load('Pause Button Icon.png')
pause = pygame.transform.scale(pause, (50, 50))

def draw():
    for item in drawable:
        item.draw()
        screen.blit(text,
        (315 - text.get_width() // 2, 10 - text.get_height() // 5))
    DISPLAY.blit(play, (275, 325))
    DISPLAY.blit(pause, (175, 325))
    pygame.display.flip()

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
                        image = Gimg
                    elif item.command == "sweater":
                        mixer.init()
                        mixer.music.load("Sweater Weather.wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                        image = SWimg
                    elif item.command == "riptide":
                        mixer.init()
                        mixer.music.load("Riptide.wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                        image = Rimg
                    elif item.command == "worth":
                        mixer.init()
                        mixer.music.load("Worth It.wav")
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                        image = WIimg
                    if item.command == "pause":
                        pygame.mixer.music.pause()
                    if item.command == "unpause":
                        pygame.mixer.music.unpause()
        DISPLAY.fill((225, 227, 231))
        DISPLAY.blit(image, (200, 70))
    draw()

pygame.quit()
