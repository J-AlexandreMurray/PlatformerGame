# import module pygame

import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption('First Py 2D Animation Test')

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')

# character base model
x = 20
y = 40
width = 20
height = 50
vel = 5

clock = pygame.time.Clock()

left = False
right = False
walkCount = 0

isJump = False
jumpCount = 10

def redrawGameWindow():
    global walkCount

    # background image drawn at point
    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:  # if we are facing left
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1

    elif right:  # if we are facing right
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1

    else:
        win.blit(char, (x, y))  # if character is standing still

    pygame.display.update()

# main game-loop
run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():  # loop through keyboard/mouse events
        if event.type == pygame.QUIT:
            run = False  # ends game loop

    keys = pygame.key.get_pressed()  # dict where key = 1 (pressed) or 0 (not pressed)

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1000 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not (isJump):  # check user for jump
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 1000 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -7:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:  # This will execute if our jump is finished
            jumpCount = 7
            isJump = False
            # Variable Reset
    redrawGameWindow()

pygame.quit()  # if exit loop game will close
