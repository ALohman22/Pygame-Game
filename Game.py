import pygame
import time
import random
import sys

WIDTH, HEIGHT = 1000, 800
X_POSITION, Y_POSITION = 500, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Happy Cube')

BG = pygame.transform.scale(pygame.image.load('Floor.jpg'), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
SHELF_HEIGHT = 20
SHELF_WIDTH = 500
START = HEIGHT - PLAYER_HEIGHT
PLAYER_VEL = 5

JUMPING = False
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

def draw(player, shelf):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, "green", player)
    pygame.draw.rect(WIN, "black", shelf)
    pygame.display.update()


def main():
    run = True 

    player = pygame.Rect(X_POSITION, Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
    shelf = pygame.Rect(0,400, SHELF_WIDTH, SHELF_HEIGHT)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            JUMPING = True

        if JUMPING:
            Y_POSITION -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                JUMPING = False
                Y_VELOCITY = JUMP_HEIGHT
        if keys[pygame.K_LEFT]:
            if player.x > 0:
                player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]:
            if player.x < WIDTH - PLAYER_WIDTH:
                player.x += PLAYER_VEL
        

       

     
        
    

if __name__ == "__main__":
    main()