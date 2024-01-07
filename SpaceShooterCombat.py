import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

backGroundMusic = mixer.Sound("D:\\Python Projects\\Projects\\Space Shooter Combat\\Music\\BackgroundMusic.mp3")
backGroundMusic.play(-1)  # -1 for loop forever, 0 for

gameOverMusic = mixer.Sound("D:\\Python Projects\\Projects\\Space Shooter Combat\\Music\\GameOver.mp3")

screenWidth, screenHeight = 800, 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Space Shooter Combat")

icon = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\SpaceShooterCombatIcon.webp")
pygame.display.set_icon(icon)

backGround = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\SpaceShooterBg.jpg")
backGround = pygame.transform.scale(backGround, (screenWidth, screenHeight))

spaceShipImage = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\spaceShip.png")
spaceShipImage = pygame.transform.scale(spaceShipImage, (screenWidth/8, screenHeight/8))

spaceShipX = screenWidth/2.5
spaceShipY = screenHeight/1.2
changeX = 0

enemiesImage = []
enemyX = []
enemyY = []
enemySpeedX = []
enemySpeedY = []
enemyNum = 6

for i in range (enemyNum):    
    enemiesImg = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\enemies.png")
    enemiesImg = pygame.transform.scale(enemiesImg, (screenWidth/10, screenHeight/10))
    enemiesImage.append(enemiesImg)

    enemyX.append(random.randint(0,int(screenWidth-screenWidth/10)))
    enemyY.append(random.randint(int(screenHeight/60), int(screenHeight/8)))

    enemySpeedX.append(0.5) 
    enemySpeedY.append(10)

bulletImage = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\bullet.png")
bulletImage = pygame.transform.scale(bulletImage,(screenWidth/18, screenHeight/18))

bulletX = screenWidth/2.3
bulletY = screenHeight-screenHeight/4.48

check = False
playing = True

score = 0

font = pygame.font.SysFont('Arial', 32, 'bold')
gameOver = pygame.font.SysFont('Arial', 72, 'bold')

gameEnd = False

def enemiesAttack():  
    # For each enemy in range of enemyNum
    for i in range(enemyNum):
        # Display enemy on screen
        screen.blit(enemiesImage[i], (enemyX[i], enemyY[i]))
    
def eliminateEnemy():
    global score
    global check
    global bulletY
    for i in range(enemyNum):
        # formula to find the distance between 2 points √(x1 - y1)² + (x2 - y2)²
        distance = math.sqrt(math.pow((enemyX[i] - bulletX), 2) + math.pow((enemyY[i] - bulletY ), 2))
        if distance < 27:
            explosionSound = mixer.Sound('D:\\Python Projects\\Projects\\Space Shooter Combat\\Music\\Explosion.mp3')     
            explosionSound.play()       
            return True
        
def spaceShip():
    # global spaceShipX, spaceShipY for accessing from anywhere
    global spaceShipX
    global spaceShipY  

    # Draw the spaceShip image at the (spaceShipX, spaceShipY) coordinates  
    screen.blit(spaceShipImage,(spaceShipX, spaceShipY))

def bullet():
    # blit bullet image on screen
    global bulletX
    global bulletY
    screen.blit(bulletImage, (bulletX, bulletY))

def playerScore():
    # Create score image using font and score variable
    scoreImage = font.render(f'Score : {score}', True, 'white')

    # Blit score image on the screen at (10, 10) coordinates
    screen.blit(scoreImage, (10, 10))

def gameOverText():   
    global backGroundMusic
    global gameOverMusic   
    # Create 'Game Over' text    
    gameOverImage = font.render('Game Over', True, 'white')
    
    # Position the text on the screen
    screen.blit(gameOverImage, (screenWidth/2.4, screenHeight/2))

    backGroundMusic.stop()
    # mixer.music.load('D:\\Python Projects\\Projects\\Music\\GameOver.mp3')
    # if gameEnd:   
    #     mixer.music.play()
    #     #pygame.time.Clock().tick(10)
    #     while mixer.music.get_busy():
    #         pygame.time.Clock().tick(10)
    #         mixer.music.stop()

def gameOverSound():
    # global gameOverMusic
    gameOverMusic = mixer.Sound("D:\\Python Projects\\Projects\\Space Shooter Combat\\Music\\GameOver.mp3")    
    gameOverMusic.play(loops=1, maxtime=1)


while playing:           
    #blit method helps to draw something on the screen
    screen.blit(backGround,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
                
        if event.type == pygame.KEYDOWN: #KeyDown : when we press the key
            if event.key == pygame.K_LEFT:
                changeX -= 1
            if event.key == pygame.K_RIGHT:
                changeX = 1
            if gameEnd == False:
                if event.key == pygame.K_SPACE:
                    if not check:
                        bulletSound = mixer.Sound('D:\\Python Projects\\Projects\\Space Shooter Combat\\Music\\BulletShoot.mp3')
                        bulletSound.play()

                        check = True
                        bulletX = spaceShipX + 27.82 #bulletX - spaceShipX = 27.82
        
        if event.type == pygame.KEYUP: #KeyUp : when we release the key
            changeX = 0        
    
    spaceShip()
    spaceShipX += changeX
    if spaceShipX <= 0:
        spaceShipX = 0
    elif spaceShipX >= screenWidth - screenWidth/8:
        spaceShipX = screenWidth - screenWidth/8

    enemiesAttack()
    for i in range(enemyNum):
        if enemyY[i] > screenHeight - screenHeight/3.8:
            gameEnd = True
            for j in range(enemyNum):
                enemyY[j] =20000
            spaceShipY =20000
            gameOverText()
            gameOverSound()
            # gameOverMusic.stop()
            break            

        enemyX[i] += enemySpeedX[i]
        if enemyX[i] <= 0:
            enemySpeedX[i] = 1
            enemyY[i] += enemySpeedY[i]
        if enemyX[i] >= (screenWidth-screenWidth/10):
            enemySpeedX[i] -= 1
            enemyY[i] += enemySpeedY[i]
        
        collide = eliminateEnemy()
        if collide:
            bulletY = screenHeight-screenHeight/4.48
            check = False
            enemyX[i] = random.randint(0,int(screenWidth-screenWidth/10))
            enemyY[i] = random.randint(int(screenHeight/60), int(screenHeight/4))
            score += 1      
        
    if check:
        bullet()
        bulletY -= 1.5
    if bulletY <= 0:
        bulletY = screenHeight - screenHeight/4.48
        check=False

    playerScore()
    pygame.display.update()