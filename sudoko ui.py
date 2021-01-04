# THIS CODE IS A SIMPLE CODE ON A GRID. THIS IS A VERY SIMPLE ALGO AND IS USED IN LITERALLY EVERY SINGLE GAME. PLEASE DELETE THIS IF READ. 
import pygame
import random
import sys





pygame.init()

width = 500
height = 500
Screen_of_device = pygame.display.set_mode((width,height))


def drawgrid():
    row = column = 9
    width_of_row = width // row
    height_of_column = height//column


    a = 0
    b = 0
    for i in range(row):
        a += width_of_row
        pygame.draw.line(Screen_of_device, pygame.Color("blue"),(a,0),(a,height))
    for i in range(column):
        b += height_of_column
        pygame.draw.line(Screen_of_device, pygame.Color("blue"), (0,b), (width,b))


def main():

    fps = 40
    clock = pygame.time.Clock()


    while True:

        Screen_of_device.fill(pygame.Color("white")) # Colour doesnt really matter here
        drawgrid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        pygame.display.update()

main()