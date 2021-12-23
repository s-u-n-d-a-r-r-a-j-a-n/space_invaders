import pygame
import math
import random

#initalising the pygame
pygame.init()

#creating the screen(width, height)
screen=pygame.display.set_mode((800,600))

#background
background=pygame.image.load('background.png')

#creating icon and title
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#adding the player and image
#Player
playerimg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerX_change=0
def player(x,y):
    screen.blit(playerimg,(x,y))
    
#enemy
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

#bullet
bulletimg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=1
bullet_state= "ready"
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))

#collision detection
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

#game over text
over_font=pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(x,y))
    
    
    
    
    

#game loop
running=True
while running:
    #background color RGB
    screen.fill((0,0,0))#black
    #background image
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        #keyword input control and key pressed event    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change= -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change= 0.1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
                
                
    playerX += playerX_change                
    
    
    #adding boundary to our game
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736
        
    #enemy moment mechanism
    for i in range(num_of_enemies):
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemy[j]=2000
            game_over_text()
            break
        enemyX[i]+= enemyX_change[i]    
        if enemyX[i] <=0:
            enemyX_change[i] = 0.1
            enemyY[i]+= enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -0.1
            enemyY[i]+= enemyY_change[i]
        #collision
        collision= iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bullet=480
            bullet_state="ready"
            score_value += 1
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)         
    
    #bullet moment
    if bulletY<=0:
        bulletY=480
        bullet_state ="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
        
        
   
    player(playerX,playerY)#function call
    show_score(textX,textY)
    
    #updating the screen
    pygame.display.update()
