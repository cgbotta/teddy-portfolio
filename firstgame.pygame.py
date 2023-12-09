import pygame
pygame.init() # initialise
clock = pygame.time.Clock()


# Need to setup our screen, first we need to pick a size 
w = 500
h = 500
fps = 10000000000000000000000000000000

screen = pygame.display.set_mode((w, h))

# Let's make our player
player = pygame.Rect((250, 250, 50, 50))
font = pygame.font.SysFont(None, 25)

def show_text( msg, color, x, y ):
  global screen
  text = font.render( msg, True, color)
  screen.blit(text, ( x, y ) )

# Part 2: Game Loop
running = True
while running == True:
  screen.fill((2,250,20,0.5))  
  pygame.draw.rect(screen,(6,129,2),player)

  #Move the player
  key = pygame.key.get_pressed()
  if key[pygame.K_w] == True:
    player.move_ip(0, -1)
   
  if key[pygame.K_a] == True:
    player.move_ip(-1, 0)
  if key[pygame.K_s] == True:
    player.move_ip(0, 1)
  if key[pygame.K_d] == True:
      player.move_ip(1, 0)

  # Check if the square is off the screen
  if player.left < 0:
    player.left = 0
  if player.right > w:
    player.right = w
  if player.top < 0:
    player.top = 0
  if player.bottom > h:
    player.bottom = h
  
  
  fps = clock.get_fps()
  
  clock.tick(fps)
 
  show_text(str(round( fps,1))+"fps", (3,3,200), 10, 10)

  # Part 3: Event Handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()  
  
pygame.quit()
