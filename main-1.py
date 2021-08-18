import pygame
import os
import random
import math


# =============================Game variablse=================================
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!Pygame variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
pygame.init()
font = pygame.font.Font("comic.ttf", 35)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Game Window!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
screenWidth = 800
screenHight = 800
title = "Solowmoooooo"
display = pygame.display.set_mode((screenHight,screenWidth))
pygame.display.set_caption(title)
ruuning = True
FPS = 25
clock = pygame.time.Clock()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!Player variables!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
playerPositionX = 212
playerPositionY = 212
playerVelocityX = 0
playerVelocityY = 2
playerSize = 20
playerSpeed = 10
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Food variables!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
foodSize = 15
foodAmount = 1
# FoodPositionX = random.randint(0,screenWidth-foodSize) 
# FoodPositionY = random.randint(0,screenHight-foodSize) 
FoodPositionX = 20
FoodPositionY = screenHight/2
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Foe variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

foeAmount = 10
minFoeDistaint = 150
foeSize = 25

#Foe moving variables
possiableWayX = random.randint(5,6)
possiableWayY = random.randint(5,6)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Color variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
black =(0,0,0)
red = (255,0,0)
green = (0,255,0)
bule = (0,0,255)
cyan = (0,255,255)
white = (255,255,255)
yellow = (255,255,0)
pink = (255,0,255)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Gride variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
grideSize = 100
deflutgrideSize = 50
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Time variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
a = 0
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Load images!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (screenWidth, screenHight)) 

gress = pygame.image.load("gress.png")
gress = pygame.transform.scale(gress, (deflutgrideSize, deflutgrideSize)) 

solid = pygame.image.load("solid.png")
solid = pygame.transform.scale(solid, (deflutgrideSize, deflutgrideSize)) 

sky = pygame.image.load("sky.png")
sky = pygame.transform.scale(sky, (deflutgrideSize, deflutgrideSize)) 

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Game variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Game variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Game variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Game variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



def main():
    global ruuning,playerVelocityX,playerPositionX,playerPositionY,playerVelocityY,foeList,a

    foeList = foeGen()
    foodList = foodGen()
    while ruuning:
        display.fill(black)
        buildLevel(worldData=worldData)

        playerWindowArea()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ruuning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ruuning = False
                # Player movements 
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    playerVelocityX = -playerSpeed
                    playerVelocityY = 0

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    playerVelocityY = playerSpeed
                    playerVelocityX = 0

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    playerVelocityX = playerSpeed
                    playerVelocityY = 0

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    playerVelocityY = -playerSpeed
                    playerVelocityX = 0

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    playerVelocityX = 0

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    playerVelocityY = 0

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    playerVelocityX = 0

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    playerVelocityY = 0

        playerPositionX += playerVelocityX
        playerPositionY += playerVelocityY
        player()
        # displayFood(foodList)
        # displayFoe(foeList,moveFoe=False,foeSheap='rect')
        # foeCollaition('rect')
        blockCollaitions(worldData)
        text_screen(f'Time:{a}',white,10,10)
        a+=1
        # drawGride()
        clock.tick(FPS)
        pygame.display.update()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])

def calculateDistance(x1,y1,x2,y2):
    global dist
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # print(dist)
    return dist
# _______________

def player():

    # pygame.draw.circle(display, green, (playerPositionX,playerPositionY), playerSize, width=0)
    pygame.draw.rect(display, green, (playerPositionX,playerPositionY,playerSize,playerSize), width=0)



foeList = []
def foeGen():
    for i in range(foeAmount):
        aFoe = []
        x = random.randint(15,screenHight-15)
        y = random.randint(15,screenWidth-15)
        if x != FoodPositionX and y != FoodPositionY:
            aFoe.append(x)
            aFoe.append(y)
            aFoe.append(random.randint(5,7))
            aFoe.append(random.randint(5,7))
            foeList.append(aFoe)

    return foeList
    

foodList = []
def foodGen():
    for i in range(foodAmount):
        aFoe = []
        x = random.randint(15,screenHight-15)
        y = random.randint(15,screenWidth-15)
        if x != FoodPositionX and y != FoodPositionY:
            aFoe.append(x)
            aFoe.append(y)
            aFoe.append(random.randint(5,7))
            aFoe.append(random.randint(5,7))
            foodList.append(aFoe)

    return foodList
    
def displayFoe(foeList,moveFoe=False,foeSheap='circle'):
    # vec = pygame.math.Vector2
    for j in foeList:
        if foeSheap == 'circle':

            pygame.draw.circle(display, red, (j[0],j[1]), foeSize, width=0)

        # Showing foe in rect
        elif foeSheap == 'rect':
            pygame.draw.rect(display, red, (j[0],j[1],40,40), foeSize, 1) #!importent

        # movement of Foes
        if moveFoe:

            if j[0] > screenWidth-foeSize:
                j[2] = random.randint(5,7)*-1

            if j[0] < 0+foeSize:
                j[2] = j[2]*-1

            if j[1] > screenHight - foeSize:
                j[3] = random.randint(5,7)*-1

            if j[1] < 0+foeSize:
                j[3] = j[3]*-1


            j[0] += j[2]
            j[1] += j[3]

        #draw conncetion to player
        # pygame.draw.line(display, white, (playerPositionX,playerPositionY), (j[0],j[1]), width=1) #!importent
        


def blockCollaitions(worldData):
    global playerVelocityY
    nearestFoe = []
    for foePostions in worldData:
        if abs(playerPositionX - foePostions[1]) < minFoeDistaint and abs(playerPositionY - foePostions[2]) < minFoeDistaint:
            
            distUpLeft = calculateDistance(playerPositionX,playerPositionY,foePostions[1],foePostions[2])

            distMid = calculateDistance(playerPositionX,playerPositionY,foePostions[1]+foeSize,foePostions[2]+foeSize)

            distUpRight = calculateDistance(playerPositionX,playerPositionY,foePostions[1]+foeSize*2,foePostions[2])

            distDownLeft = calculateDistance(playerPositionX,playerPositionY,foePostions[1],foePostions[2]+foeSize*2)

            distDwonRight = calculateDistance(playerPositionX,playerPositionY,foePostions[1]+foeSize*2,foePostions[2]+foeSize*2)
        
            # Shoe rect foe connections.........
            pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[1],foePostions[2]), width=1)

            pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[1]+foeSize,foePostions[2]+foeSize), width=1)

            pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[1]+foeSize*2,foePostions[2]), width=1)

            pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[1],foePostions[2]+foeSize*2), width=1)

            pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[1]+foeSize*2,foePostions[2]+foeSize*2), width=1)


            # 1 Find the nearest node
            NfoeInto = []
            NfoeInto.append(distMid)
            NfoeInto.append(foePostions[1])
            NfoeInto.append(foePostions[2])
            nearestFoe.append(NfoeInto)

            #storing all collection dist
            collectionDist = []
            collectionDist.append(distUpLeft)
            collectionDist.append(distDwonRight)
            collectionDist.append(distMid)
            collectionDist.append(distUpRight)
            collectionDist.append(distDownLeft)
            
            # sorting the collectionDist
            collectionDist.sort()
            # print(dist)
            lowerPoint = playerSize + foeSize
            # print(lowerPoint,distUpLeft,distMid,distUpRight)
            if distMid <= lowerPoint:
                # print(collectionDist[0])
                pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)
                playerVelocityY = 0

                if distUpLeft < playerSize+foeSize/2:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)
                        
                if distUpRight < playerSize+foeSize/2:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                if distDownLeft < playerSize+foeSize/2:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                if distDwonRight < playerSize+foeSize/2:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

            if distMid >= int(lowerPoint)+2:
                if distUpLeft < playerSize:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)
                        
                if distUpRight < playerSize:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                if distDownLeft < playerSize:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                if distDwonRight < playerSize:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

    nearestFoe.sort()
    try:
        # print(nearestFoe[0])
        pass
        # pygame.draw.line(display, white, (playerPositionX,playerPositionY), (nearestFoe[0][1],nearestFoe[0][2]), width=1)
    except IndexError:
        pass
    return nearestFoe.sort()

    pass



def foeCollaition(foeSheap):
    global foeList
    nearestFoe = []
    for foePostions in foeList:
        if abs(playerPositionX - foePostions[0]) < minFoeDistaint and abs(playerPositionY - foePostions[1]) < minFoeDistaint:
            if foeSheap == 'circle':
                dist = calculateDistance(playerPositionX,playerPositionY,foePostions[0],foePostions[1])
                # Shoe circle foe connections.........
                pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[0],foePostions[1]), width=1)
                # pygame.draw.line(display, white, (FoodPositionX,FoodPositionY), (foePostions[0],foePostions[1]), width=1)
                # print(angle_of_line(playerPositionX,playerPositionY,foePostions[0],foePostions[1]))

                NfoeInto = []
                NfoeInto.append(dist)
                NfoeInto.append(foePostions[0])
                NfoeInto.append(foePostions[1])
                nearestFoe.append(NfoeInto)

                if dist < playerSize+foeSize:
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)
            
            elif foeSheap == 'rect':
                distUpLeft = calculateDistance(playerPositionX,playerPositionY,foePostions[0],foePostions[1])

                distMid = calculateDistance(playerPositionX,playerPositionY,foePostions[0]+foeSize,foePostions[1]+foeSize)

                distUpRight = calculateDistance(playerPositionX,playerPositionY,foePostions[0]+foeSize*2,foePostions[1])

                distDownLeft = calculateDistance(playerPositionX,playerPositionY,foePostions[0],foePostions[1]+foeSize*2)

                distDwonRight = calculateDistance(playerPositionX,playerPositionY,foePostions[0]+foeSize*2,foePostions[1]+foeSize*2)
            
                # Shoe rect foe connections.........
                pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[0],foePostions[1]), width=1)

                pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[0]+foeSize,foePostions[1]+foeSize), width=1)

                pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[0]+foeSize*2,foePostions[1]), width=1)

                pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[0],foePostions[1]+foeSize*2), width=1)

                pygame.draw.line(display, white, (playerPositionX,playerPositionY), (foePostions[0]+foeSize*2,foePostions[1]+foeSize*2), width=1)


                # 1 Find the nearest node
                NfoeInto = []
                NfoeInto.append(distMid)
                NfoeInto.append(foePostions[0])
                NfoeInto.append(foePostions[1])
                nearestFoe.append(NfoeInto)

                #storing all collection dist
                collectionDist = []
                collectionDist.append(distUpLeft)
                collectionDist.append(distDwonRight)
                collectionDist.append(distMid)
                collectionDist.append(distUpRight)
                collectionDist.append(distDownLeft)
                
                # sorting the collectionDist
                collectionDist.sort()
                # print(dist)
                lowerPoint = playerSize + foeSize
                print(lowerPoint,distUpLeft,distMid,distUpRight)
                if distMid <= lowerPoint+2:
                    # print(collectionDist[0])
                    pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                    if distUpLeft < playerSize+foeSize/2:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)
                            
                    if distUpRight < playerSize+foeSize/2:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                    if distDownLeft < playerSize+foeSize/2:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                    if distDwonRight < playerSize+foeSize/2:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                if distMid >= int(lowerPoint):
                    if distUpLeft < playerSize:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)
                            
                    if distUpRight < playerSize:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                    if distDownLeft < playerSize:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

                    if distDwonRight < playerSize:
                        pygame.draw.circle(display, red, (playerPositionX,playerPositionY), playerSize, width=0)

    nearestFoe.sort()
    try:
        # print(nearestFoe[0])
        pass
        # pygame.draw.line(display, white, (playerPositionX,playerPositionY), (nearestFoe[0][1],nearestFoe[0][2]), width=1)
    except IndexError:
        pass
    return nearestFoe.sort()

# Get the angel of nearest node
def movePlayer(nodeList=list):
    global playerPositionY,playerPositionX,playerVelocityX,playerVelocityY
    nearestNodeAngel = (angle_of_line(playerPositionX,playerPositionY,nodeList[0],nodeList[1]))
    



def displayFood(foodList):
    playerFoodConncetion()
    pygame.draw.circle(display, pink, (FoodPositionX,FoodPositionY), foodSize, width=0)
    for j in foodList:
        pygame.draw.circle(display, pink, (j[0],j[1]), foodSize, width=0)




def playerWindowArea():
    global playerVelocityX,playerVelocityY,playerPositionX,playerPositionY
    if playerPositionX > screenWidth - playerSize:
        playerVelocityX = 0
        playerPositionX = playerPositionX - playerSize

    if playerPositionX < 0 + playerSize:
        playerVelocityX = 0
        playerPositionX = 0 + playerSize

    if playerPositionY > screenHight - playerSize:
        playerVelocityY = 0
        playerPositionY = screenHight - playerSize

    if playerPositionY < 0 + playerSize:
        playerVelocityY = 0
        playerPositionY = 0 + playerSize


def playerFoodConncetion():
    pygame.draw.line(display,  white, (playerPositionX,playerPositionY), (FoodPositionX,FoodPositionY), width=4)


# 1 gride = 50x50
def drawGride(showgride = True):
    global lineNumberX,lineNumberY
    grideSize = deflutgrideSize
    lineNumberX = screenWidth / grideSize 
    lineNumberY = screenHight / grideSize
    if showgride:

        for i in range(round(lineNumberX)):
            pygame.draw.line(display, white, (grideSize,0), (grideSize,screenHight), 1)
            grideSize += deflutgrideSize
        grideSize = deflutgrideSize

        
        for i in range(round(lineNumberY)):
            pygame.draw.line(display, white, (0,grideSize), (screenWidth,grideSize), 1)
            grideSize += deflutgrideSize

        grideSize = deflutgrideSize

        
    return [round(lineNumberX),round(lineNumberY)]


def angle_of_vector(x, y):
    #return math.degrees(math.atan2(-y, x))            # 1: with math.atan
    return pygame.math.Vector2(x, y).angle_to((1, 0))  # 2: with pygame.math.Vector2.angle_to
    
def angle_of_line(x1, y1, x2, y2):
    #return math.degrees(math.atan2(-y1-y2, x2-x1))    # 1: math.atan
    return angle_of_vector(x2-x1, y2-y1)               # 2: pygame.math.Vector2.angle_to
    



def buildLevel(worldData=list):

    for item in worldData:
        display.blit(item[0],(item[1],item[2]))

def loadLevel(levedata=list):
    worldData = []
    rowNumber = 0
    for row in levedata:
        for index, gride in enumerate(row):

            if gride == 1:
                sg = []
                sg.append(gress)
                sg.append((index)*deflutgrideSize)
                sg.append(rowNumber)
                worldData.append(sg)

            elif gride == 2:
                sg = []
                sg.append(solid)
                sg.append((index)*deflutgrideSize)
                sg.append(rowNumber)
                worldData.append(sg)

            elif gride == 3:
                sg = []
                sg.append(sky)
                sg.append((index)*deflutgrideSize)
                sg.append(rowNumber)
                worldData.append(sg)
        rowNumber += deflutgrideSize
    
    return worldData

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Level variablse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
level1 = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0],
            [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

worldData = loadLevel(level1)

def jump():
    global playerVelocityY,playerPositionY,jumpNow,jumpSpeed,jumpTakeOffposition,jumpTime
    




if __name__ == "__main__":
    main()











