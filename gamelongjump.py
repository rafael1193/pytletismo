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
from playerjumper import Jumper
import pausemenu

class Gamelongjump:

    def __init__(self):
        self._mousepos = (0, 0)
        self._LEFT = 1
        self._player=Jumper([pygame.image.load("img/muñecajo.png"),pygame.image.load("img/muñecajo2.png")],45,240,0, [pygame.K_s, pygame.K_l])
        self._fondo = pygame.image.load("img/dibujo2.png").convert()
        self._band = pygame.image.load("img/banda.png").convert_alpha()
        self._fuente = pygame.font.SysFont('sans', 25, False, False)
        self._message = ""
        self._renderedmessage = None
        self._jumpline = 700 - 32
        self._running = True
        self._time = 0

    def play(self, screen, clock):
        while self._running:
            #events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    sys.exit(0)
                elif event.type == pygame.MOUSEMOTION:
                    self._mousepos = event.pos
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        c = pausemenu.Pausemenu(['Volver al juego','Reiniciar', u'Salir al menú principal'])
                        result = c.show(screen,clock)
                        if result == 'Volver al juego':
                            pass
                        if result == 'Reiniciar':
                            self.restart()
                        elif result == u'Salir al menú principal':
                            self._running = False
                            return
                    if event.key == self._player.keys[0] and self._player.state == 'running':
                        self._player.speed=self._player.speed + 0.1
                        self._player.nextframe()
                    elif event.key == self._player.keys[1] and self._player.state == 'running':
                        self._player.state = 'jumping'
                        self._time=0
                        self._player.nextframe()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self._LEFT:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP and event.button == self._LEFT:
                    print "You released the left mouse button at (%d, %d)" % event.pos

            #update
            self._time += 1
            self._player.update(self._time)
            if self._player.x >= self._jumpline and self._player.state == 'running':
                self._player.state = 'stopping'
                #print "salto nulo"
                self._message = "Salto nulo"
                self._renderedmessage = self._fuente.render(self._message, True, (255, 255, 255)).convert_alpha()
            if self._player.state == 'landed':
                #print "Has saltado %s pixeles" % (self._player.x - self._jumpline)
                if self._player.x - self._jumpline < 0:
                    self._message = "Salto nulo"
                    self._renderedmessage = self._fuente.render(self._message, True, (255, 255, 255)).convert_alpha()
                    self._player.state = 'end'
                else:
                    self._message = u"Has saltado " + str(int(round(self._player.x)) - self._jumpline) + u" píxeles"
                    self._renderedmessage = self._fuente.render(self._message, True, (255, 255, 255)).convert_alpha()
                    self._player.state = 'end'

            #drawing
            pygame.display.flip()
            screen.fill((0, 0, 0))
            screen.blit(self._fondo, (0,0))
            screen.blit(self._band, (0, 0))
            if self._renderedmessage is not None:
                screen.blit(self._renderedmessage, (self._fondo.get_width() / 2 - self._renderedmessage.get_width() / 2, self._band.get_height() / 2 - self._renderedmessage.get_height() / 2))
            else:
                rendered = self._fuente.render(u"Corre con 'S' y salta antes de la línea con 'L'", True, (255,255,255))
                screen.blit(rendered, (self._fondo.get_width() / 2 - rendered.get_width() / 2, self._band.get_height() / 2 - rendered.get_height() / 2))
            screen.blit(self._player.currentframe(),(self._player.x,self._player.y))

            #clock
            clock.tick(60)
        return

    def restart(self):
        self.__init__()
