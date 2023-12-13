import pygame
import random
clock = pygame.time.Clock()

pygame.init()


# Need to setup our screen, first we need to pick a size 
w = 500
h = 500

#Create the screen
screen = pygame.display.set_mode((w, h))
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 600)
     
# Here is where we make our player
class Player(pygame.sprite.Sprite):
  def __init__(self):
      super(Player, self).__init__()
      self.surf = pygame.Surface((75, 25))
      self.surf.fill((255, 24, 255))
      self.rect = self.surf.get_rect()
  def update(self, key):
      if key[pygame.K_w] == True:
        self.rect.move_ip(0, -10)
      if key[pygame.K_a] == True:
        self.rect.move_ip(-10, 0)
      if key[pygame.K_s] == True:
        self.rect.move_ip(0, 10)
      if key[pygame.K_d] == True:
        self.rect.move_ip(10, 0)
     
    
      if self.rect.left < 0:
        self.rect.left = 0
      if self.rect.right > w:
        self.rect.right = w
      if self.rect.top < 0:
        self.rect.top = 0
      if self.rect.bottom > h:
        self.rect.bottom = h


player = Player()

# Here is where we make our enemy
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
      super(Enemy, self).__init__()
      self.surf = pygame.Surface((25, 25))
      self.surf.fill((25, 224, 25))
      starting_x = w + 100
      starting_y = random.randint(0, h)
      self.rect = self.surf.get_rect(center=(starting_x, starting_y))
      self.speed = 10
  def update(self):
      self.rect.move_ip(self.speed * -1, 0)

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game Loop
running = True
while running == True:
  
  # Event Handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == ADD_ENEMY:
      enemy = Enemy()
      enemies.add(enemy)
      all_sprites.add(enemy)
      
      
  player.update(pygame.key.get_pressed())
  enemies.update()

  screen.fill((0 ,0 , 0))  

  for sprite in all_sprites:
    screen.blit(sprite.surf, sprite.rect)

  # Check for collisions
  if pygame.sprite.spritecollideany(player, enemies):
    player.kill()
    running = False

  pygame.display.flip()
  clock.tick(30)


pygame.quit()
