# _*_coding:utf-8_*_
import os
import pygame

'''
文字转图片,haha...
'''
pygame.init()
# 新建画布
surface = pygame.Surface((500, 420))
# 设置字体
font = pygame.font.Font('simhei.ttf', 14)

with open('text.txt', 'r', encoding='utf-8') as f:
    # 读取每一行的文字和索引
    for i, line in enumerate(f.readlines()):
        # 创建字体对象
        textSurface = font.render(line, True, (255, 255, 255), (0, 0, 0))
        # 创建字体图层
        textRec = textSurface.get_rect()
        # 设置字体图层显示的中心
        textRec.center = (255, (i + 1) * 30)
        # 在画布上显示
        surface.blit(textSurface, textRec)

pygame.image.save(surface, 'test.jpg')
