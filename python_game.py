
#导入相关的库或包
import pygame
import sys
import random

#全局定义
SCREEN_X = 600
SCREEN_Y = 600  


#创建蛇类
class Snake:
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = [ ]
    
        for x in range(5):
            self.addnode()

    def addnode(self):
        left,top = (0,0)
        if self.body:
            left ,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left,top,25,25)
        if self.dirction == pygame.K_LEFT:
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0,node)
        
    def delnode(self):
        self.body.pop()
    
    #死亡判断
    def isdead(self):
        #撞墙
        if self.body[0].x not in range(SCREEN_X):
            return True
        if self.body[0].y not in range(SCREEN_Y):
            return True
        #撞自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    #移动
    def move(self):
        self.addnode()
        self.delnode()

    #改变方向
    def changedirction(self,curkey):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD =[pygame.K_UP,pygame.K_DOWN]
        if curkey in LR+UD:
            if (curkey in LR) and (self.dirction in LR):
                return
            if (curkey in UD) and (self.dirction in UD):
                return
            self.dirction = curkey


#创建食物
class Food:
    def __init__(self):
        self.rect = pygame.Rect(-25,0,25,25)

    def remove(self):
        self.rect.x = -25

    def set(self):
        if self.rect.x == -25:
            allpos = []
            #不靠近墙近25 ~SCREEN_X-25之间
            for pos in range(25,SCREEN_X - 25,25):
                allpos.append(pos)
                self.rect.left = random.choice(allpos)
                self.rect.top = random.choice(allpos)
                print(self.rect)

#画面加载
def show_text(screen,pos,text,color,font_bold = False,font_size = 60,font_italic = False):
    #获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体",font_size)
    #设置是否加粗属性
    cur_font.set_bold(font_bold)
    #设置是否斜体属性
    cur_font.set_italic(font_italic)
    #设置文字内容
    text_fmt = cur_font.render(text ,1,color)
    #绘制文字
    screen.blit(text_fmt,pos)


#游戏初始化
def main():
    pygame.init()
    screen_size = (SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("贪吃蛇")    #窗口标题
    clock = pygame.time.Clock()
    scores = 0
    isdead = False


    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.changedirction(event.key)
                if event.key == pygame .K_SPACE and isdead:
                    return main()
      
        screen.fill((255,255,255))

        #画蛇身
        if not isdead:
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen,(20,220,39),rect,0)

        #显示文字内容
        isdead = snake.isdead()

        #显示死亡的界面
        if isdead:
            show_text(screen,(100,200),"YOU DEAD",(227,29,18),False,100)
            show_text(screen,(150,260),"空白键 to try again...",(0,0,22),False,30)

        #食物的处理  吃到+50分  （食物与蛇头   蛇身长度+1方块
        if food.rect == snake.body[0]:
            scores += 50
            food.remove()
            snake.addnode()

        food.set()
        pygame.draw.rect(screen,(136,0,21),food.rect,0)

        #显示分数文字
        show_text(screen,(50,500), str(scores),(223,223,223))

        pygame.display.update()
        clock.tick(10)


main()
