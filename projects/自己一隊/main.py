# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:22:40 2014

@author: user
"""

class Brick(object):
    """
    ...
    enum bgcolor,wdcolor,word
    bool banished
    """
    def __init__(this,bgc,wdc,wd):
        this.bgcolor=bgc
        this.wdcolor=wdc
        this.word=wd
        this.banished=False
    def show(this,x,y):
        if this.bgcolor==-1:
            return
        coord=(16+x*32,544-48-y*32)
        global ftime
        global banishTime
        global banish
        if x==-10:
            coord=(311,169)
        if this.banished:
            screen.blit(banish,coord,(32*(banishTime/6),0,32,32))
        else:
            screen.blit(bgData[this.bgcolor],coord)
            screen.blit(wdData[this.word][this.wdcolor],coord)
        
def conflict(coord):
    x=coord[0]
    y=coord[1]
    xa=0
    while controlBricks[2-xa][2]!=noBrick:
        xa+=1
        if(xa==3):break
    xb=0
    while controlBricks[2+xb][2]!=noBrick:
        xb+=1
        if(xb==3):break
    ya=0
    while controlBricks[2][2-ya]!=noBrick:
        ya+=1
        if(ya==3):break
    yb=0
    while controlBricks[2][2+yb]!=noBrick:
        yb+=1
        if(yb==3):break
    if x-xa<-1 or x+xb>=maxX+1:
        return True
    if y-ya<-1 or y+yb>=maxY+1:
        return True
    
    for cx in range(5):
        for cy in range(5):
            if controlBricks[cx][cy]!=noBrick:
                if bricks[x-2+cx][y-2+cy]!=noBrick:
                    return True
    return False

def banishX(x,y,bgc,bonus):
    for bx in range(bgc):
        bricks[x-bx][y].banished=True
        if bonus:
            if y<maxY-1:
                bricks[x-bx][y+1].banished=True
            if y>0:
                bricks[x-bx][y-1].banished=True
    if bonus:
        if x<maxX-1:
            bricks[x+1][y].banished=True
        if x-bgc>=0:
            bricks[x-bgc][y].banished=True

def banishY(x,y,bgc,bonus):
    global changeBonus
    for by in range(bgc):
        bricks[x][y-by].banished=True
        if bonus:
            if x<maxX-1:
                bricks[x+1][y-by].banished=True
            if x>0:
                bricks[x-1][y-by].banished=True
    if bonus:
        if y<maxY-1:
            bricks[x][y+1].banished=True
        if y-bgc>=0:
            bricks[x][y-bgc].banished=True
        changeBonus=True

def check():
    global mode
    rec=False
    if mode==0:
        for y in range(maxY):
            bgc=1
            wdc=1
            wcc=1
            for x in range(maxX)[:-1]:
                if bricks[x][y].bgcolor==bricks[x+1][y].bgcolor:
                    bgc+=1
                else:
                    if bgc>=3 and bricks[x][y]!=noBrick:
                        banishX(x,y,bgc,bricks[x][y].bgcolor==bonusBrick.word)
                        rec=True
                    bgc=1
                    
                if bricks[x][y].word==bricks[x+1][y].word:
                    wdc+=1
                else:
                    if wdc>=3 and bricks[x][y]!=noBrick:
                        banishX(x,y,wdc,bricks[x][y].word==bonusBrick.bgcolor)
                        rec=True
                    wdc=1
            if bgc>=3 and bricks[maxX-1][y]!=noBrick:
                banishX(maxX-1,y,bgc,bricks[maxX-1][y].bgcolor==bonusBrick.word)
                rec=True
            if wdc>=3 and bricks[maxX-1][y]!=noBrick:
                banishX(maxX-1,y,wdc,bricks[maxX-1][y].word==bonusBrick.bgcolor)
                rec=True
        for x in range(maxX):
            bgc=1
            wdc=1
            wcc=1
            for y in range(maxY)[:-1]:
                if bricks[x][y].bgcolor==bricks[x][y+1].bgcolor:
                    bgc+=1
                else:
                    if bgc>=3 and bricks[x][y]!=noBrick:
                        banishY(x,y,bgc,bricks[x][y].bgcolor==bonusBrick.word)
                        rec=True
                    bgc=1
    
                if bricks[x][y].word==bricks[x][y+1].word:
                    wdc+=1
                else:
                    if wdc>=3 and bricks[x][y]!=noBrick:
                        banishY(x,y,wdc,bricks[x][y].word==bonusBrick.bgcolor)
                        rec=True
                    wdc=1
            if bgc>=3 and bricks[x][maxY-1]!=noBrick:
                banishY(x,maxY-1,bgc,bricks[x][maxY-1].bgcolor==bonusBrick.word)
                rec=True
            if wdc>=3 and bricks[x][maxY-1]!=noBrick:
                banishY(x,maxY-1,wdc,bricks[x][maxY-1].word==bonusBrick.bgcolor)
                rec=True
    else:
        for y in range(maxY):
            b=True
            for x in range(maxX):
                if bricks[x][y]==noBrick:
                    b=False
                    break
            if b:
                banishX(0,y,maxX,False)
                rec=True
    if rec:
        global BANISH
        global status
        global banishTime
        status=BANISH
        banishTime=0

def rotate():
    global control
    global controlBricks
    x=control[0]
    y=control[1]
        
    for cx in range(3):
        for cy in range(2):
            bx=4-cx
            by=4-cy
            temp=controlBricks[cx][cy]
            controlBricks[cx][cy]=controlBricks[by][cx]
            controlBricks[by][cx]=controlBricks[bx][by]
            controlBricks[bx][by]=controlBricks[cy][bx]
            controlBricks[cy][bx]=temp
            
    if(conflict(control)):
        for cx in range(3):
            for cy in range(2):
                bx=4-cx
                by=4-cy
                temp=controlBricks[cx][cy]
                controlBricks[cx][cy]=controlBricks[cy][bx]
                controlBricks[cy][bx]=controlBricks[bx][by]
                controlBricks[bx][by]=controlBricks[by][cx]
                controlBricks[by][cx]=temp

def putBrick():
    global control
    x=control[0]
    y=control[1]
    for cx in range(5):
        for cy in range(5):
            if controlBricks[cx][cy]!=noBrick:
                bricks[x-2+cx][y-2+cy]=controlBricks[cx][cy]
                controlBricks[cx][cy]=noBrick

def newBrick():
    global control
    global controlBricks
    nbList=(
        (4,(0,2),(1,2),(2,2),(2,3)),
        (4,(4,2),(3,2),(2,2),(2,3)),
        (4,(3,3),(3,2),(2,2),(2,3)),       
        (4,(0,2),(1,2),(2,2),(3,2)),
        (4,(3,2),(1,2),(2,2),(2,3)),       
        (3,(1,2),(2,2),(3,2)),
        (3,(1,2),(2,2),(2,3)),
        (2,(1,2),(2,2)),
        (1,(2,2))
        )
    if mode==0:
        i=int(random()*9)
    else:
        i=int(random()*5)
    for j in range(nbList[i][0]):
        controlBricks[nbList[i][j+1][0]][nbList[i][j+1][1]]=Brick(int(random()*4),0,int(random()*4))
#    controlBricks[2][3]=Brick(0,0,0)
    control=(maxX/2,maxY-2)
    
    
#==============================================================================
noBrick=Brick(-1,-1,-1)

fin=open("score.txt","rt")
hiScore=[]
hiScore.append(int(fin.readline()))
hiScore.append(int(fin.readline()))
fin.close()

maxX=8
maxY=16

PLAY=0
BANISH=1
GAMEOVER=2
PAUSE=3
banishTime=0

import pygame
pygame.init()

bgData=[]
wdData=[]
for i in range(4):
    bgData.append(pygame.image.load("bg"+str(i)+".bmp"))
    wdData.append([])
    for j in range(4):
        wdData[i].append(pygame.image.load("wd"+str(i)+"-"+str(0)+".png"))
background=pygame.image.load("background.bmp")
banish=pygame.image.load("scatter.png")
gameover=pygame.image.load("gameover.png")
timer=pygame.image.load("timer.png")

size = (416, 544)
screen = pygame.display.set_mode(size)


mode=0
changeMode=False
done = False
while not done:
    bricks=[]
    for x in range(maxX):
        bricks.append([])
        for y in range(maxY):
            bricks[x].append(noBrick)
    
    controlBricks=[[noBrick]]
    for x in range(5):
        if x>=1:
            controlBricks.append([noBrick])
        for y in range(5)[1:]:
            controlBricks[x].append(noBrick)
            
    control=(2,maxY-2)
    newBrick()
    bonusBrick=Brick(int(random()*4),0,int(random()*4))
    
    status=PLAY
    score=0
    changeBonus=False
    
    if changeMode:
        if mode==0:mode=1
        else: mode=0
        changeMode=False
    
    ftime=0
    tpf=24
    retry =False
    while (not done) and (not retry):
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done=True
                if event.key == pygame.K_r:
                    retry=True
                if event.key == pygame.K_m:
                    retry=True
                    changeMode=True
                if  status==PAUSE:
                    if event.key == pygame.K_p:
                        status=PLAY
                elif  status==PLAY:
                    if event.key == pygame.K_RIGHT:
                        if not conflict((control[0]+1,control[1])):
                            control=(control[0]+1,control[1])
                    elif event.key == pygame.K_LEFT:
                        if not conflict((control[0]-1,control[1])):
                            control=(control[0]-1,control[1])
                    elif event.key == pygame.K_UP:
                        rotate()
                    elif event.key == pygame.K_DOWN:
                        tpf=3;
                    elif event.key == pygame.K_p:
                        status=PAUSE
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    tpf=24
        if status==PLAY :
            if(ftime % tpf == 0):
                if not conflict((control[0],control[1]-1)):
                    control=(control[0],control[1]-1)
                else:
                    putBrick()
                    check()
                    newBrick()
                    if conflict(control):
                        status=GAMEOVER
                        
        
        screen.fill((14,35,147))
        screen.blit(background,(0,0))
        
        for x in range(maxX):
            for y in range(maxY):
                bricks[x][y].show(x,y)
        for x in range(5):
            for y in range(5):
                controlBricks[x][y].show(control[0]+x-2,control[1]+y-2)
        for x in range(5):
            n=(hiScore[mode]/(10**x)) %10
            screen.blit(timer,(400-16-x*20,33),(n*16,0,16,33))
        for x in range(5):
            n=(score/(10**x)) %10
            screen.blit(timer,(400-16-x*20,101),(n*16,0,16,33))
        bonusBrick.show(-10,-10)
        if status==GAMEOVER:
            screen.blit(gameover,(16,(544-128)/2))
        pygame.display.flip();
        pygame.time.wait(15)
        if(status==PLAY):
            ftime+=1
        elif(status==BANISH):
            banishTime+=1
            if(banishTime>=24):
                for x in range(maxX):
                    sy=0
                    for y in range (maxY):
                        if (not bricks[x][y].banished) or bricks[x][y]==noBrick:
                            bricks[x][sy]=bricks[x][y]
                            sy+=1
                    score+=(maxY-sy)*10
                    for y in range(maxY)[sy:]:
                        bricks[x][y]=noBrick
                status=PLAY
                banishTime=0
                check()
                if status==PLAY and changeBonus:
                    bonusBrick=Brick(int(random()*4),0,int(random()*4))
                    changeBonus=False
#=================== End of While 2 ===========================================
    if score>hiScore[mode]:
        hiScore[mode]=score
fout=open("score.txt","wt")
fout.write(format(hiScore[0]))
fout.write('\n')
fout.write(format(hiScore[1]))
fout.close()

pygame.quit()
