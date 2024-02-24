import pygame
import random
pygame.init()

w = 500
h = 500
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()



rect = pygame.Rect(135, 220, 30, 30)
velocity = 5
jump = False
jumpCount = 0
jumpMax = 15




running = True
while running == True:
    clock.tick(50)
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jump:
        #   jump = jump + 1
        #   if jump > jumpCount:
        #     jump = jump - 1
        #   else:
        #     jump = jump + 1  
            jump = True
            jumpCount = jumpMax
        
    if jump:
    rect.y = rect.y - jumpCount
    if jumpCount > -jumpMax:
        jumpCount = jumpCount - 1
    else:
        jump = False

    pygame.draw.rect(screen, (64, 64, 64), (0, 250, 300, 100))
    pygame.draw.circle(screen, (255, 0, 0), rect.center, 15)
    pygame.display.flip()
            
        
        

        

pygame.quit()
