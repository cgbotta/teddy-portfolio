import pygame
import random
clock = pygame.time.Clock()
score = 0
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)
enemy_spawn_rate = 400
enemy_speed = 1


# Need to setup our screen, first we need to pick a size 
w = 500
h = 500

#Create the screen
screen = pygame.display.set_mode((w, h))

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, enemy_spawn_rate)

ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 10000)
# Here is where we make our player
class Player(pygame.sprite.Sprite):
  def __init__(self):
      super(Player, self).__init__()
      self.surf = pygame.image.load("jet.png").convert()
      self.surf.set_colorkey((255,255,255), pygame.RLEACCEL)
      # self.surf = pygame.Surface((75, 25))
      # self.surf.fill((255, 24, 255))
      self.rect = self.surf.get_rect()
  def update(self, key):
      if key[pygame.K_w] == True:
        self.rect.move_ip(0, -10 - enemy_speed/3)
      if key[pygame.K_a] == True:
        self.rect.move_ip(-10 - enemy_speed/3, 0)
      if key[pygame.K_s] == True:
        self.rect.move_ip(0, 10 + enemy_speed/3)
      if key[pygame.K_d] == True:
        self.rect.move_ip(10 +enemy_speed/3, 0)
     
    
      if self.rect.left < 0:
        self.rect.left = 0
      if self.rect.right > w:
        self.rect.right = w
      if self.rect.top < 0:
        self.rect.top = 0
      if self.rect.bottom > h:
        self.rect.bottom = h


player = Player()
class Cloud(pygame.sprite.Sprite):
  def __init__(self):
      super(Cloud, self).__init__()
      self.surf = pygame.image.load("cloud.png").convert()
      self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
      starting_x = w + 100
      starting_y = random.randint(0, h)
      self.rect = self.surf.get_rect(center=(starting_x, starting_y))
      
      self.speed = 4
  def update(self):
      self.rect.move_ip(self.speed * -1, 0)
# Here is where we make our enemy
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
      super(Enemy, self).__init__()
      self.surf = pygame.image.load("missile.png").convert()
      self.surf.set_colorkey((255,255,255), pygame.RLEACCEL)
      starting_x = w + 100
      starting_y = random.randint(0, h)
      self.rect = self.surf.get_rect(center=(starting_x, starting_y))
      enemy_speed = 4 + score/10 
      if enemy_speed > 25:
        enemy_speed = 25
      self.speed = enemy_speed
  def update(self):
      self.rect.move_ip(self.speed * -1, 0)
    
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
clouds = pygame.sprite.Group()
# Game Loop
running = True
while running == True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == ADD_ENEMY:
      enemy = Enemy()
      enemies.add(enemy)
      all_sprites.add(enemy)
      score = score + 1
    elif event.type == ADD_CLOUD:
      cloud = Cloud()
      clouds.add(cloud)
      all_sprites.add(cloud)
      score = score + 20
  
  # enemy_numbers = len(enemies)
  # if enemy_numbers < 5:
  #   enemy_spawn_rate = 1
  # else:
  #   enemy_spawn_rate = 1000
  # pygame.time.set_timer(ADD_ENEMY, enemy_spawn_rate)
  player.update(pygame.key.get_pressed())
  enemies.update()
  clouds.update()
  screen.fill((0 ,0 , 200))  

  score_text = font.render("Score: "+ str(score), True, (255, 255, 255) )
  screen.blit(score_text,(10, 10))
  if enemy_speed > 15:
    enemy_speed = 15
  for sprite in all_sprites:
    screen.blit(sprite.surf, sprite.rect)
  
  # Check for collisions
  if pygame.sprite.spritecollideany(player, enemies):
    player.kill()
    running = False

  pygame.display.flip()
  clock.tick(30)


pygame.quit()
