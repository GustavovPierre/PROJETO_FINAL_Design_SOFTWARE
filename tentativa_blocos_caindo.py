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
import time

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
pygame.display.set_caption('Crazy Pelican')
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
 
    
    
#aviao = Aviao("Bomb-image.png", 250, 150, randrange(1), randrange(1))    
#class Bomb(pygame.sprite.Sprite):
#    
#    def __init__(self, width, height):
#        super().__init__()
#        self.image = pygame.Surface([width, height])
#        self.rect = self.image.get_rect()
#        
#    def reset_pos(self):
#        
#        self.rect.y = random.randrange(-300, -20)
#        self.rect.x = random.randrange(0, 600)
#        
#    def update(self):
#
#        # Move block down one pixel
#        self.rect.y += 1
# 
#        # If block is too far down, reset to top of screen.
#        if self.rect.y > 410:
#            self.reset_pos()
# 
#bomb_list = pygame.sprite.Group()
#all_sprites_list = pygame.sprite.Group()    
#
#for i in range(50):
#    # This represents a block
#    bomb = Bomb(20, 15)
# 
#    # Set a random location for the block
#    bomb.rect.x = random.randrange(600)
#    bomb.rect.y = random.randrange(800)
# 
#    # Add the block to the list of objects
#    bomb_list.add(bomb)
#    all_sprites_list.add(bomb)
# Define some colors
BLACK = (0, 0, 0)
class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        
        self.rect.y = random.randrange(-500, -20)
        self.rect.x = random.randrange(0, 600)
 
    def update(self):
      
        # Move block down one pixel
        self.rect.y += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.reset_pos()

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(600)
    block.rect.y = random.randrange(800)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

    # Calls update() method on every sprite in the list
all_sprites_list.update()
 
        # Reset block to the top of the screen to fall again.
block.reset_pos()
 
    # Draw all the spites
all_sprites_list.draw(tela)
 
    # Limit to 20 frames per second
clock.tick(20)

    #
pygame.display.flip()
 

    
    

pygame.display.quit()