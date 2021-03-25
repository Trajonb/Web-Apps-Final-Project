# Trajon Brown
# 3/25/2021
# Game for webpage in web apps

import pygame
import time
import random

pygame.init()

# colors
blue = (0, 0, 255)
orange = (255, 100, 10)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
orange = (255, 100, 10)

# display coordinates
display_width = 800
display_height = 600

# game display
pygame.display.set_caption('Trajon and Zaylie')
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# Car Image
carImage = pygame.image.load('zaylie.png')
car_width = 70


# car method for the position of the car
def car(x, y):
    gameDisplay.blit(carImage, (x, y))


# bot image method
def objects(object_x, object_y, object_width, object_height, color):
    trajon = pygame.image.load('trajon.png')
    gameDisplay.blit(trajon, [object_x, object_y, object_width, object_height])


# Score Function
def objects_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score :" + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


# Button
def button(msg, x, y, w, h, inactiveColor, activeColor, action=None):
    mouse = pygame.mouse.get_pos()
    mouseclick = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, activeColor, (x, y, w, h))
        if mouseclick[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactiveColor, (x, y, w, h))

    goText = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textRect = text_objects(msg, goText)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textsurf, textRect)


# Game Menu
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        background_img = pygame.image.load('sun_moon.png')
        gameDisplay.fill(yellow)
        largeText = pygame.font.Font('freesansbold.ttf', 55)
        TextSurf, TextRect = text_objects("Trajon and Zaylie Game", largeText)
        TextRect.center = ((410), (25))
        gameDisplay.blit(background_img, (200, 50))
        gameDisplay.blit(TextSurf, TextRect)

        button("Go!", 100, 450, 100, 60, blue, blue, game_loop)
        button("Quit", 600, 450, 100, 60, orange, orange, game_quit)

        pygame.display.update()
        clock.tick(10)


# game loop
def game_loop():
    # position of car
    x = (display_width * 0.4)
    y = (display_height * 0.75)

    x_left = 0
    x_right = 0

    # obects parameters
    object_start_x = random.randrange(0, display_width)
    object_start_y = -600
    object_speed = 2
    object_height = 75
    object_width = 100

    # Objects Dodged
    dodged = 0

    # Game Logic
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():  # For closing the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # when a key is pressed down
                if event.key == pygame.K_LEFT:  # left arrow key
                    x_left = -5
                if event.key == pygame.K_RIGHT:  # right arrow key
                    x_right = +5

            if event.type == pygame.KEYUP:  # when the key is released
                if event.key == pygame.K_LEFT:  # left arrow key
                    x_left = 0
                if event.key == pygame.K_RIGHT:  # right arrow key
                    x_right = 0

        # change the position of the car
        x += x_left
        x += x_right

        # white background
        gameDisplay.fill(yellow)

        # objects location
        objects(object_start_x, object_start_y, object_width, object_height, blue)
        object_start_y += object_speed

        car(x, y)
        objects_dodged(dodged)

        if x > (display_width - car_width) or x < 0:  # if the car goes outside the boundary
            crashed()

        if object_start_y > display_height:  # object repeats itself
            object_start_y = 0 - object_height
            object_start_x = random.randrange(0, display_width)
            dodged += 5
            if object_speed <= 9.9:
                object_speed += 0.1
            if object_width <= 199.5:
                object_width += (dodged * 0.5)

        if y < object_start_y + object_height:  # object crash logic

            if x > object_start_x and x < object_start_x + object_width or x + car_width > object_start_x and x + car_width < object_start_x + object_width:
                crashed()

        pygame.display.update()
        clock.tick(220)


# Quit Game
def game_quit():
    pygame.quit()
    quit()


# crashed method
def crashed():
    crashed_message('Crashed!!')


# text objects
def text_objects(message, font):
    text = font.render(message, True, black)
    return text, text.get_rect()


# crashed message
def crashed_message(message):
    large_text = pygame.font.Font('freesansbold.ttf', 75)
    text_surface, text_rectangle = text_objects(message, large_text)
    text_rectangle.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surface, text_rectangle)
    pygame.display.update()
    time.sleep(2)
    game_loop()


game_intro()
game_loop()
