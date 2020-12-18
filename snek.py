import pygame
import sys
import time
import random
from pygame import event


class Snake:
    difficulty = 5

    frame_size_x = 720
    frame_size_y = 480

    check_errors = pygame.init()

    if check_errors[1] > 0:
        sys.exit(-1)
    pygame.display.set_caption('The Snake Game')

    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    black = pygame.Color(0, 0, 0)
    yellow = pygame.Color(255, 255, 0)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(61, 235, 223)

    speed = pygame.time.Clock()
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    food_pos = [random.randrange(1, (frame_size_x//10))
                * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0

    def game_over(self):
        my_font = pygame.font.SysFont('arial', 90)
        game_over_surface = my_font.render('Game Over :(', True, Snake.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (
            (Snake.frame_size_x)/2, (Snake.frame_size_y)/4)
        Snake.game_window.fill(Snake.black)
        Snake.game_window.blit(game_over_surface, game_over_rect)
        Snake.show_score(self, 0, Snake.red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render(
            'Score : ' + str(Snake.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (Snake.frame_size_x/10, 15)
        else:
            score_rect.midtop = (Snake.frame_size_x/2, Snake.frame_size_y/1.25)
        Snake.game_window.blit(score_surface, score_rect)

    def game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        Snake.change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        Snake.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        Snake.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        Snake.change_to = 'RIGHT'
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            if Snake.change_to == 'UP' and Snake.direction != 'DOWN':
                Snake.direction = 'UP'
            if Snake.change_to == 'DOWN' and Snake.direction != 'UP':
                Snake.direction = 'DOWN'
            if Snake.change_to == 'LEFT' and Snake.direction != 'RIGHT':
                Snake.direction = 'LEFT'
            if Snake.change_to == 'RIGHT' and Snake.direction != 'LEFT':
                Snake.direction = 'RIGHT'
            if Snake.direction == 'UP':
                Snake.snake_pos[1] -= 10
            if Snake.direction == 'DOWN':
                Snake.snake_pos[1] += 10
            if Snake.direction == 'LEFT':
                Snake.snake_pos[0] -= 10
            if Snake.direction == 'RIGHT':
                Snake.snake_pos[0] += 10
            Snake.snake_body.insert(0, list(Snake.snake_pos))
            if Snake.snake_pos[0] == Snake.food_pos[0] and Snake.snake_pos[1] == Snake.food_pos[1]:
                Snake.score += 1
                Snake.difficulty += 1
                Snake.food_spawn = False
            else:
                Snake.snake_body.pop()
            if not Snake.food_spawn:
                Snake.food_pos = [random.randrange(
                    1, (Snake.frame_size_x//10)) * 10, random.randrange(1, (Snake.frame_size_y//10)) * 10]
            Snake.food_spawn = True
            Snake.game_window.fill(Snake.black)
            for Snake.pos in Snake.snake_body:
                pygame.draw.rect(Snake.game_window, Snake.blue,
                                 pygame.Rect(Snake.pos[0], Snake.pos[1], 10, 10))
            pygame.draw.rect(Snake.game_window, Snake.yellow, pygame.Rect(
                Snake.food_pos[0], Snake.food_pos[1], 10, 10))
            if Snake.snake_pos[0] < 0 or Snake.snake_pos[0] > Snake.frame_size_x-10:
                Snake.game_over(self)
            if Snake.snake_pos[1] < 0 or Snake.snake_pos[1] > Snake.frame_size_y-10:
                Snake.game_over(self)
            for Snake.block in Snake.snake_body[1:]:
                if Snake.snake_pos[0] == Snake.block[0] and Snake.snake_pos[1] == Snake.block[1]:
                    Snake.game_over(self)

            Snake.show_score(self, 1, Snake.yellow, 'times new roman', 20)
            pygame.display.update()
            Snake.speed.tick(Snake.difficulty)

        # while True:
        ##    op=input("Do you want to play (y/n)")
        # op=op.lower()
        # if op=='y':
        # game()
        # else:
        ##        print("Thank You!")
        # break


Snake().game()
