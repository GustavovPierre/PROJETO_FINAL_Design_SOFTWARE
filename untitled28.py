# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:44:00 2018

@author: 2000
"""

import pygame
import pygame as pg
import sys
from pygame.locals import *
from random import randrange

class Aviao(pygame.sprite.Sprite):
  def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
    pygame.sprite.Sprite.__init__(self)

    self.vx = vel_x
    self.vy = vel_y
    self.image = pygame.image.load(arquivo_imagem)
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y
    
  def move(self):
    self.rect.x += self.vx
    self.rect.y += self.vy
    

pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Air Rescue')

background = pygame.image.load("cartoon_clouds-wallpaper-800x600.png").convert()

# Cria bola e adiciona em um grupo de Sprites.
aviao = Aviao("Webp.net-resizeimage.png", 250, 150, randrange(1), randrange(1))
aviao_group = pygame.sprite.Group()
aviao_group.add(aviao)


# ===============   LOOPING PRINCIPAL   ===============
rodando = True
while rodando:

    # === PRIMEIRA PARTE: LIDAR COM EVENTOS ===

    # Para cada evento não-processado na lista de eventos:
    for event in pygame.event.get():
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False


    aviao.move()

    if aviao.rect.x < -95:
        aviao.rect.x = 805
    if aviao.rect.x > 805:
        aviao.rect.x = -95

    if aviao.rect.y < 0:
        aviao.rect.y= 0
    if aviao.rect.y > 490:
        aviao.vx = 490
        
        aviao.rect.y = 0
    if aviao.rect.y > 490:
        aviao.rect.y = 490
        
    keyinput = pg.key.get_pressed()
    
    if keyinput[pg.K_LEFT]:
        aviao.rect.x -= 1
    elif keyinput[pg.K_RIGHT]:
        aviao.rect.x += 1
    elif keyinput[pg.K_UP]:
        aviao.rect.y -= 1
    elif keyinput[pg.K_DOWN]:
        aviao.rect.y += 1


    tela.blit(background, (0, 0))
    aviao_group.draw(tela)
    pygame.display.update()

pygame.display.quit()