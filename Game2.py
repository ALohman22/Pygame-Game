import pygame
pygame.init()

win = pygame.display.set_mode((1000, 800))

pygame. display.set_caption('Something')

width = 60
height = 60
vel = 5
x = 500
y = 800 - height

isJump = False
jumpCount = 10

run = True
while run:
    win.fill(('White'))
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
     
    player = pygame.draw.rect(win, ('Green'), (x, y, width, height))
    obsticle = pygame.draw.rect(win, ('Black'), (400, 650, 400, 40))

    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= vel
    if keys[pygame.K_RIGHT]:
        if x < 1000 - width:
            x += vel
    if player.colliderect(obsticle):
        y == 600
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                 neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
            

    pygame.display.update()

pygame.quit()