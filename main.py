import pygame
import random

pygame.init()

#Техехнические переменные
display_height = 600
display_width = 800
display = pygame.display.set_mode((display_width, display_height))
icon = pygame.image.load("icon.png")
clock = pygame.time.Clock()


pygame.display.set_caption("Run Dino! Run!")
pygame.display.set_icon(icon)


#Классы
#Класс Кактуса(Противник)
class Cactus:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.iamge = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.iamge, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.iamge = image
        display.blit(self.iamge, (self.x, self.y))


#Переменные
#Переменные Дино(Игрок)
usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 100

#Переменные Кактуса(Противник)
cactus_width = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100
cactus_image = [pygame.image.load("cactus.png"), pygame.image.load("cactus.png")]
cactus_options = [64, 408, 64, 408]

#Переменные Прыжка(Функция игрока)
make_jump = False
jump_counter = 30


#Функции
#Главная функция игры
def run_game():
    global make_jump, usr_x, usr_y, usr_height
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)
    land = pygame.image.load("land.png")
    
    #Проверка на выход
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Проверка на перемеещения
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            make_jump = True

        if keys[pygame.K_LEFT]:
            usr_x -= 5

        if keys[pygame.K_RIGHT]:
            usr_x += 5

        if make_jump:
            jump()

        #Отрисовка объектов
        display.blit(land, (0, 0))
        draw_array(cactus_arr)
        pygame.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_width, usr_height))

        pygame.display.update()

        clock.tick(80)

#Функция Прыжка
def jump():
    global usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False

#Функция создание Кактусов
def create_cactus_arr(array):
    choice = random.randrange(0, 2)
    img = cactus_image[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Cactus(display_width + 20, height, width, img, 4))
    
    choice = random.randrange(0, 2)
    img = cactus_image[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Cactus(display_width + 300, height, width, img, 4))
    
    choice = random.randrange(0, 2)
    img = cactus_image[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Cactus(display_width + 600, height, width, img, 4))

#Функция поиска Радиуса
def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice ==0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)

    return radius

#Фнкция отрисовки Кактусов
def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            radius = find_radius(array)
            
            choice = random.randrange(0, 2)
            img = cactus_image[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]
            
            cactus.return_self(radius, height, width, img)

run_game()