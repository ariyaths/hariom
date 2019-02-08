import pygame
import random as r
# import time


pygame.init()

display_width = 800
display_height = 600

gameScreen = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
clock = pygame.time.Clock()
FPS = 15

pygame.display.set_caption("OldSnake")


def message_to_screen(msg, type):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, type)
    gameScreen.blit(screen_text, [display_width / 2, display_height / 2])


def our_snake(lead_x, lead_y, size_of_block):

    pygame.draw.rect(gameScreen, green, (lead_x, lead_y, 10, 10))


def game_loop():
    game_close = False
    game_over = False

    size_of_block = 10
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []
    snake_length = 1
    rand_apple_x = round(r.randrange(0, display_width - size_of_block) / 10) * 10
    rand_apple_y = round(r.randrange(0, display_height - size_of_block) / 10) * 10

    lead_x = display_width / 2
    lead_y = display_height / 2

    while not game_close:
        while game_over == True:
            gameScreen.fill(white)
            message_to_screen("Game over, Press Enter to play again or Q to quit.", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False

                    if event.key == pygame.K_KP_ENTER:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -size_of_block
                    lead_y_change = 0

                elif event.key == pygame.K_RIGHT:
                    lead_x_change = size_of_block
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    lead_y_change = -size_of_block
                    lead_x_change = 0

                elif event.key == pygame.K_DOWN:
                    lead_y_change = size_of_block
                    lead_x_change = 0

            lead_x += lead_x_change
            lead_y += lead_y_change
            if lead_x >= 800 or lead_x <= 10 or lead_y >= 600 or lead_y <= 10:
                game_over = True

        gameScreen.fill(white)
        pygame.draw.rect(gameScreen, red, (rand_apple_x, rand_apple_y, 10, 10))
        pygame.draw.rect(gameScreen, green, (lead_x, lead_y, 10, 10))
        pygame.display.update()
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = round(r.randrange(0, display_width - size_of_block) / 10) * 10
            rand_apple_y = round(r.randrange(0, display_height - size_of_block) / 10) * 10
            # our_snake(size_of_block, snake_list)
        clock.tick(FPS)

    # message_to_screen("You loose.", red)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()
    quit()


game_loop()
