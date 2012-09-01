#!/usr/bin/env python
# -*- coding: utf-8 *-*

###############################################################################
#    Pytletismo
#    Copyright (C) 2012  Rafael Bailón-Ruiz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

import pygame
import sys
from menu import Menu
from credits import Credits
from game100m import Game100m
from gamelongjump import Gamelongjump
from game110mhurdles import Game110mhurdles

pygame.font.init()

running = 1

screen = pygame.display.set_mode((1024, 600))
pygame.display.set_caption('Pytletismo')
clock = pygame.time.Clock()
mousepos = (0, 0)
LEFT = 1

#p1=Player([pygame.image.load("j2a.bmp"),pygame.image.load("j2b.bmp")],0,13,0)
#p2=Player([pygame.image.load("j1a.bmp"),pygame.image.load("j1b.bmp")],40,350,0)
p1imahora = 1
#fondo = pygame.image.load("estadio.bmp")

#Menu
#menu = Menu(['100m lisos','110m vallas', 'Salto de longitud', None, u'Créditos', 'Salir'])
menu = Menu(['100m lisos', 'Salto de longitud', None, u'Créditos', 'Salir'])
while True:
    game = menu.show(screen, clock)

    if game == 'Salir':
        #print 'Salir'
        sys.exit(0)
    elif game == u'Créditos':
        #print 'Créditos'
        play = Credits()
        play.play(screen, clock)
    elif game == '100m lisos':
        #print '100m lisos'
        play = Game100m()
        play.play(screen, clock)
    elif game == '110m vallas':
        #print '110m vallas'
        play = Game110mhurdles()
        play.play(screen, clock)
    elif game == 'Salto de longitud':
        #print 'Salto de longitud'
        play = Gamelongjump()
        play.play(screen, clock)

##Game
#print '100m lisos'
#while running:
#    #events
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = 0
#        elif event.type == pygame.MOUSEMOTION:
#            mousepos = event.pos
#        elif event.type == pygame.KEYDOWN:
#            pressedkeys = pygame.key.get_pressed()
#            if pressedkeys[pygame.K_l]:
#                p1.x=p1.x+5
#                p1imahora=p1imahora*-1
#            if pressedkeys[pygame.K_v]:
#                p2.speed=p2.speed+0.1
#        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
#            p1.x=p1.x+3
#            p1imahora=p1imahora*-1
#        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
#            print "You released the left mouse button at (%d, %d)" % event.pos
#    p2.update()
#    #drawing
#    pygame.display.flip()
#    screen.fill((0, 0, 0))
#    screen.blit(fondo,(0,0))
#    #screen.blit(fuente.render('Holaaaa',True,(255,255,255)),(30,30))
#    if p1imahora == 1:
#        screen.blit(p1.image[0],(p1.x,p1.y))
#    else:
#        screen.blit(p1.image[1],(p1.x,p1.y))
#
#    screen.blit(p2.image[0],(p2.x,p2.y))
#
#    #clock
#    clock.tick(100)
#
