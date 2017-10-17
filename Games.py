import pygame as pg


def checkCollision(x,y,treasureX,treasureY):
    global screen,textWin
    collisionState =False
    if y>=treasureY and y<=treasureY+40:
        if x >= treasureX and x <= treasureX+35:
            y=650
            collisionState=True
        elif x+35 >=treasureX and x+35 <=treasureX+35:
            y=650
            collisionState=True
    elif y + 40 >= treasureY and y + 40<= treasureY + 40:
        if x>=treasureX and  x<=treasureX+35:
            y=650
            collisionState=True
        elif x+35>=treasureX and x+35<=treasureX+35:            
            y=650
            collisionState=True
    return collisionState,y


pg.init()
screen  = pg.display.set_mode((900,700))

finished = False
x=450-35/2
y=650
array = []
playerImage = pg.image.load("Player.png")
playerImage = pg.transform.scale(playerImage,(35,40))
playerImage = playerImage.convert_alpha()
bgImage = pg.image.load("background.png")
bgImage = pg.transform.scale(bgImage,(900,700))
#screen.blit(bgImage,(0,0))

treasureImage = pg.image.load("treasure.png")
treasureImage = pg.transform.scale(treasureImage,(35,40))
treasureImage=treasureImage.convert_alpha()

enemyImage = pg.image.load("enemy.png")
enemyImage = pg.transform.scale(enemyImage,(35,40))
enemyImage = enemyImage.convert_alpha()

treasureX=450-35/2
treasureY=50

enemyX = 100
enemyY = 580-10
movingRight = True

enemies = [(enemyX,enemyY,movingRight)] 

font = pg.font.SysFont("comicsans",60)
level = 1

#dictionary = {}

enemyNames = {0:"Max",1:"Jill",2:"Grek",3:"Diane"}

frame = pg.time.Clock()
colliasionTreasure = False
colliasionEnemy = False



while finished == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished =True

    pressedKeys = pg.key.get_pressed()
    #print pressedKeys[pg.K_SPACE]
    
    enemyIndex = 0 
    for enemyX,enemyY,movingRight in enemies:
        if(enemyX >= 800-35):
            movingRight=False
        elif enemyX <=50:
            movingRight=True

        if(movingRight==True):        
            enemyX += 5*level
        else:
            enemyX -= 5*level
        enemies[enemyIndex] = (enemyX,enemyY,movingRight)
        enemyIndex +=1

    if pressedKeys[pg.K_SPACE] == 1:
        y-=5
    #rectOne = pg.Rect(x,y,30,30)

    #color = (0,0,255)
    white=(255,255,255)
    black=(0,0,0)


    screen.blit(bgImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(playerImage,(x,y))

    enemyIndex=0
    for enemyX,enemyY,movingRight in enemies:        
        screen.blit(enemyImage,(enemyX,enemyY))
        colliasionEnemy,y = checkCollision(x,y,enemyX,enemyY)        
        if (colliasionEnemy ==True):
            name = enemyNames[enemyIndex]
            textLose = font.render("You were killed by "+str(name),True,(255,0,0))
            screen.blit(textLose,(450-textLose.get_width()/2,350-textLose.get_height()/2))
            pg.display.flip()
            frame.tick(1)
        enemyIndex+=1
    #pg.draw.rect(screen ,color,rectOne)

    colliasionTreasure,y = checkCollision(x,y,treasureX,treasureY)

    
    if(colliasionTreasure==True):
        level +=1
        enemies.append((enemyX-50*level,enemyY-50*level,False))
        textWin = font.render("You've reached the next Level "+str(level),True,(0,0,0))
        screen.blit(textWin,(450-textWin.get_width()/2,350-textWin.get_height()/2))
        pg.display.flip()
        frame.tick(1)
    #elif collisionEnemy ==True:
 

    pg.display.flip()
    frame.tick(30)

    
