import pygame
import math
from random import randint
import time

# game constants
WIDTH = 640
HEIGHT = 320
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# game variables
color = RED
time_left = randint(3000, 7000) / 1000
time_elapsed = 0
stop = False

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Action")

# game functions
def draw_text(text, size, color, position):
    font = pygame.font.Font('font.ttf', size)
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)

def reset_variables():
    global color, time_left, time_elapsed, stop
    color = RED
    time_left = randint(3000, 7000) / 1000
    time_elapsed = 0
    stop = False
    

# game loop
exit = False
while not exit:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN and time_left < 0:
            stop = True
        if event.type == pygame.MOUSEBUTTONDOWN and time_left > 0:
            time_left += randint(30, 60) / 10
        if event.type == pygame.KEYDOWN and time_left < 0 and stop:
            time_left += randint(30, 60) / 10
            reset_variables()

    if time_left < 0:
        if not stop:
            color = GREEN
            time.sleep(0.001)
            time_elapsed += 0.001
        draw_text(f"{round(time_elapsed, 3)}", 96, WHITE, (WIDTH / 2, HEIGHT / 2))
        draw_text("Press any key to continue...", 24, WHITE, (WIDTH / 2, HEIGHT / 2 + 150))
    else:
        color = RED
        time.sleep(0.01)
        time_left -= 0.01
        draw_text("Wait for green...", 96, WHITE, (WIDTH / 2, HEIGHT / 2))
        draw_text("Clicking increases the wait time", 24, WHITE, (WIDTH / 2, HEIGHT / 2 + 100))

    pygame.display.update()

pygame.quit()