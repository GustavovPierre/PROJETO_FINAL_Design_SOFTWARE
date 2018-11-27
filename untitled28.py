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
import random

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
    
class Bebe(pygame.sprite.Sprite):

    def __init__(self, imagem_bebe):
        pygame.sprite.Sprite.__init__(self)
        self.y = 0
        self.x = random.randint(0,800)
        
        
        picture = pygame.transform.scale(pygame.image.load(imagem_bebe), (80, 60))
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
       self.rect.y += 1
       if self.rect.y == 600:
           self.rect.y = 0
           self.rect.x = random.randint(0,800)
           
          
            
class Missel(pygame.sprite.Sprite):

    def __init__(self, imagem_missel):
        pygame.sprite.Sprite.__init__(self)
        self.y = 0
        self.x = random.randint(0,800)
        
        picture2 = pygame.transform.scale(pygame.image.load(imagem_missel), (200, 150))
        self.image = picture2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
   
    def update(self):
       self.rect.y +=1
    
       if self.rect.y == 600:
           self.rect.y = 0
           self.rect.x = random.randint(0,800)
           

pygame.init()

preto = (0,0,0)
branco = (255,255,255)
placar = 40

#block = Block()
pygame.font.init()
font = pygame.font.SysFont(None,25, bold=True)


tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Air Rescue')

plano_de_fundo = pygame.image.load("Photoshop-Wallpaper-Raining-Cloud-800x600.png").convert()

tamanho_plano_de_fundo = plano_de_fundo.get_size()
posicao_plano_de_fundo = plano_de_fundo.get_rect()
screen = pygame.display.set_mode(tamanho_plano_de_fundo)
a,b = tamanho_plano_de_fundo
x = 0
y = 0

x1 = a
y1 = 0

def texto(msg,cor):
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1,[20, 600-placar])

# Cria bola e adiciona em um grupo de Sprites.
aviao = Aviao("PelicanoCria.png", 250, 150, randrange(1), randrange(1))
aviao_group = pygame.sprite.Group()
aviao_group.add(aviao)

bebe = Bebe("meupirudebone.png")
bebe_group = pygame.sprite.Group()
bebe_group.add(bebe)

missel = Missel("missel.png")
missel_group = pygame.sprite.Group()
missel_group.add(missel)
pontos = 0

# ===============   LOOPING PRINCIPAL   ===============
rodando = True
while rodando:
    #pos_x = random.randint(0,(800-600)/10,)*10
#    pos_y = random.randint(0,(600-800)/10,)*10
#    bebe_x = random.randint(0,(800-600)/10,)*10
#    bebe_y = random.randint(0,(600-800)/10,)*10
    
    # === PRIMEIRA PARTE: LIDAR COM EVENTOS ===

    # Para cada evento não-processado na lista de eventos:
    for event in pygame.event.get():
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False
            
    screen.blit(plano_de_fundo, posicao_plano_de_fundo)

    x1 -= 0.1
    x -= 0.1
    screen.blit(plano_de_fundo,(x,y))
    screen.blit(plano_de_fundo,(x1,y1))
    if x < -800:
        x = a
    if x1 < -800:
        x1 = a

    aviao.move()

    if aviao.rect.x < -95:
        aviao.rect.x = 800
    if aviao.rect.x > 805:
        aviao.rect.x = -90

    if aviao.rect.y < 0:
        aviao.rect.y = 0
    if aviao.rect.y > 490-placar:
        aviao.rect.y = 490-placar
        
    
        
        
        
    blocks_hit_list = pygame.sprite.spritecollide(aviao,bebe_group, True)
    for block in blocks_hit_list:
        bebe = Bebe("meupirudebone.png")
        bebe_group.add(bebe)
        
        pontos +=1
        
   
    blocks_hit_list = pygame.sprite.spritecollide(aviao,missel_group, True)
    for block in blocks_hit_list:
        missel = Missel("missel.png")
        missel_group.add(missel)
        
        pontos -=3
        
   
        
    keyinput = pg.key.get_pressed()
    
    if keyinput[pg.K_LEFT]:
        aviao.rect.x -= 1
    elif keyinput[pg.K_RIGHT]:
        aviao.rect.x += 1
    elif keyinput[pg.K_UP]:
        aviao.rect.y -= 1
    elif keyinput[pg.K_DOWN]:
        aviao.rect.y += 1

    
        
        
        
        
    pygame.draw.rect(plano_de_fundo,preto,[0,600-placar,800,placar])
    texto("Pontuação:"+str(pontos),branco)
    


    aviao_group.draw(tela)
    bebe_group.draw(tela)
    bebe_group.update()
    missel_group.draw(tela)
    missel_group.update()
    
    pygame.display.flip()
    pygame.display.update()

pygame.display.quit()