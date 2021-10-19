


import pygame


pygame.init()


screen = pygame.display.set_mode((500, 600))  # 设置主窗口大小;返回一个surface对象
screen.fill((14, 21, 154))  # 填充屏幕颜色为白色


# rect 绘制矩形
pygame.draw.rect(screen,(0,0,255),(100,100,20,30))
pygame.display.update()

# circle 绘制圆形
pygame.draw.circle(screen,(255,0,0),(200,200),30)
pygame.display.update()

# line 绘制直线
pygame.draw.line(screen, (0, 255, 0), (300, 300), (300, 500), 1)  # 最低为1
pygame.display.update()

# 使用 pygame.image.load() 加载图像的数据
bg = pygame.image.load(r'D:\soft\pycharm\work\27-pygame 入门\image1\背景.jpg')
# 使用 游戏屏幕 对象，调用 blit 方法 将图像绘制到指定位置
screen.blit(bg, (0, 0))
# 调用 pygame.display.update() 方法更新整个屏幕的显示
pygame.display.update()

apple = pygame.image.load(r'D:\soft\pycharm\work\27-pygame 入门\image1\苹果.png')
screen.blit(apple, (420, 50))
pygame.display.update()
# apple1 = pygame.image.load(r'D:\soft\pycharm\work\27-pygame 入门\image1\苹果.png')
# screen.blit(apple1, (500, 120))
# pygame.display.update()
clock = pygame.time.Clock()  # 创建时钟对象
app_rect = pygame.Rect((420, 50, 64, 64))  # 记录苹果初始位置
# i = 0

while True:
    clock.tick(60)
    app_rect.y += 1
    if app_rect.y >= 600:  # y>= 屏幕高度，将苹果移到原来位置
        app_rect.y = 50
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判断用户是否点击了关闭
            print('退出游戏……')
            pygame.quit()

            # 退出系统
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                app_rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                app_rect.x += 10



    screen.blit(bg, (0, 0))
    screen.blit(apple, app_rect)

    pygame.display.update()



#    pass

pygame.quit()




