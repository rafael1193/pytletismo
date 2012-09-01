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


class Pausemenu:
    """Game menu for Pytletismo"""
    def __init__(self, options):
        self._gameselected = False
        self._fuente = pygame.font.SysFont('sans', 30, False, False)
        self._fuentetitulo = pygame.font.SysFont('sans', 40, True, False)
        self._fuentegorda = pygame.font.SysFont('sans', 30, True, False)
        self._fondo = None
        self._fade = pygame.image.load("img/fade.png")
        self._games = options
        self._gameindex = 0
    def show(self,screen,clock):
        self._fondo = screen

        while not self._gameselected:
            #events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    pressedkeys = pygame.key.get_pressed()
                    if pressedkeys[pygame.K_UP]:
                        if self._gameindex > 0:
                            if self._games[self._gameindex - 1] != None:
                                self._gameindex = self._gameindex - 1
                            else:
                                self._gameindex = self._gameindex - 2
                    if pressedkeys[pygame.K_DOWN]:
                        if self._gameindex < len(self._games) - 1:
                            if self._games[self._gameindex + 1] != None:
                                self._gameindex = self._gameindex + 1
                            else:
                                self._gameindex = self._gameindex + 2
                    if pressedkeys[pygame.K_RETURN]:
                        self._gameselected=True
                    if pressedkeys[pygame.K_ESCAPE]:
                        return ''
            #drawing
            pygame.display.flip()
            screen.fill((0, 0, 0))

            screen.blit(self._fondo, (0, 0))
            screen.blit(self._fade, (0, 0))
            rendered = self._fuentetitulo.render("Pausa", True, (255, 128, 32))
            screen.blit(rendered, (screen.get_width() / 2 - rendered.get_width() / 2, 40))
            i = 0
            while i<=len(self._games)-1:
                if i != self._gameindex:
                    screen.blit(self._fuente.render(self._games[i],True,(200,200,200)),(160,220+i*30))
                else:
                    screen.blit(self._fuentegorda.render(self._games[i],True,(255,255,255)),(160,220+i*30))
                i=i+1

            #clock
            clock.tick(100)
        self._gameselected = False
        return self._games[self._gameindex]
