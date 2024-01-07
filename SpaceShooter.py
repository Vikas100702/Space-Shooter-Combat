import pygame
import random
import math

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)

# Set screen dimensions
WIDTH = 800
HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the screen
pygame.display.set_caption("Space Shooter")

# Set game clock
clock = pygame.time.Clock()

# Load player images
player_img = pygame.image.load('D:\\Python Projects\\Projects\\Images\\spaceShip.png')
player_img = pygame.transform.scale(player_img, (50, 50))

# Load enemy images
# enemy_img = pygame.image.load('D:\\Python Projects\\Projects\\Images\\enemies.png')
# enemy_img = pygame.transform.scale(enemy_img, (50, 50))
enemy_img = []
for i in range(5):
    img = pygame.image.load('D:\\Python Projects\\Projects\\Images\\enemies.png')
    img = pygame.transform.scale(img, (50, 50))
    enemy_img.append(img)

# Load bullet image
bullet_img = pygame.image.load('D:\\Python Projects\\Projects\\Images\\bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (10, 10))

# Load background image
background_img = pygame.image.load('D:\\Python Projects\\Projects\\Images\\SpaceShooterBg.jpg')
background_img = pygame.transform.scale(background_img,(WIDTH, HEIGHT))

# Define player position and movement speed
player_x = 370
player_y = 480
player_speed = 5

# Define enemy position and movement speed
# enemy_x = random.randint(0, 736)
# enemy_y = random.randint(50, 150)
enemy_pos = []
for i in range(5):
    x = random.randint(0, 736)
    y = random.randint(50, 150)
    enemy_pos.append([x, y])
enemy_speed = 1

# Define bullet position and movement speed
bullet_x = 0
bullet_y = 480
bullet_speed = -5

# Game variables
bullet_state = "ready"
score = 0

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    return False

# Game loop
running = True
while running:
    # Limit frames per second
    clock.tick(60)

    # Draw background
    screen.blit(background_img, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press space to fire bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player on the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    for i in range(5):
        if enemy_pos[i][1] > 430:
            enemy_pos[i][1] -= enemy_speed
        else:
            enemy_pos[i][0] = random.randint(0, 736)
            enemy_pos[i][1] = random.randint(50, 150)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y +=bullet_speed 
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

    # Collision detection
    for i in range(5):
        collision = isCollision(enemy_pos[i][0], enemy_pos[i][1], bullet_x, bullet_y)
        if collision:
            print("Collision detected!")
            bullet_y = 480
            bullet_state = "ready"
            enemy_pos[i][0] = random.randint(0, 736)
            enemy_pos[i][1] = random.randint(50, 150)

    # Draw player and enemy
    player(player_x, player_y)
    for i in range(5):
        enemy(enemy_pos[i][0], enemy_pos[i][1], i%4)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()