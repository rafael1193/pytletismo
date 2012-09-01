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
from player import Player
from hurdle import Hurdle
import pausemenu


class Game110mhurdles:

    def __init__(self):
        pygame.mixer.init()
        self._mousepos = (0, 0)
        self._LEFT = 1
        self._players=[Player([pygame.image.load("img/muñecajo.png").convert_alpha(),pygame.image.load("img/muñecajo2.png").convert_alpha()],0,215,10, [pygame.K_l]), \
        Player([pygame.image.load("img/muñecajo.png").convert_alpha(),pygame.image.load("img/muñecajo2.png").convert_alpha()],0,285,10,[pygame.K_m]), \
        Player([pygame.image.load("img/muñecajo.png").convert_alpha(),pygame.image.load("img/muñecajo2.png").convert_alpha()],0,355,10,[pygame.K_x]), \
        Player([pygame.image.load("img/muñecajo.png").convert_alpha(),pygame.image.load("img/muñecajo2.png").convert_alpha()],0,425,10,[pygame.K_a])]
        self._hurdles = [[Hurdle(pygame.image.load("valla.png"), 200, 230)], [Hurdle(pygame.image.load("img/valla.png"), 400, 230)], [Hurdle(pygame.image.load("img/valla.png"), 600, 230)],\
        [Hurdle(pygame.image.load("img/valla.png"), 200, 300)], [Hurdle(pygame.image.load("img/valla.png"), 400, 300)], [Hurdle(pygame.image.load("img/valla.png"), 600, 300)],\
        [Hurdle(pygame.image.load("img/valla.png"), 200, 370)], [Hurdle(pygame.image.load("img/valla.png"), 400, 370)], [Hurdle(pygame.image.load("img/valla.png"), 600, 370)],\
        [Hurdle(pygame.image.load("img/valla.png"), 200, 440)], [Hurdle(pygame.image.load("img/valla.png"), 400, 440)], [Hurdle(pygame.image.load("img/valla.png"), 600, 440)]]
        self._markssound = pygame.mixer.Sound("snd/preparados.wav")
        self._readysound = pygame.mixer.Sound("snd/listos.wav")
        self._gosound = pygame.mixer.Sound("snd/ya.wav")
        self._fuente = pygame.font.SysFont('sans', 25, False, False)
        self._fondo = pygame.image.load("img/dibujo.png").convert()
        self._band = pygame.image.load("img/banda.png").convert_alpha()
        self._running = True
        self._message = "Pulsa 'Y' para empezar. Corre con 'L', 'M', 'X' o 'A'"
        self._racetimemessage = None
        '''possible states: ['before', 'on your marks', 'ready', 'go', 'run', 'win']'''
        self._gamestate = "before"
        self._interval = 3000
        self._timebefore = pygame.time.get_ticks()
        self._finishline = 945
        self._racetime = 0
        self._racestart = 0

    def play(self, screen, clock):
        self._screen = screen
        self._clock = clock
        while self._running:

            self._update()
            self._draw()

            #clock
            clock.tick(60)
        return

    def _update(self):
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
                    result = c.show(self._screen,self._clock)
                    if result == 'Volver al juego':
                        pass
                    if result == 'Reiniciar':
                        self.restart()
                    elif result == u'Salir al menú principal':
                        self._running = False
                        return
                if event.key == pygame.K_y and self._gamestate == 'before':
                    self._markssound.play()
                    self._gamestate = 'on your marks'
                    self._message = "A sus puestos"
                    self._timebefore = pygame.time.get_ticks()
                    self._interval = 1500
                if self._gamestate == 'go' or self._gamestate == 'run' or self._gamestate == 'win':
                    for p in self._players:
                        if event.key == p.keys[0] and not p.bloqued:
                            p.update()
                            p.nextframe()
                elif self._gamestate != 'before':
                    for p in self._players:
                        if event.key == p.keys[0]:
                            p.bloqued = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self._LEFT:
                pass
            elif event.type == pygame.MOUSEBUTTONUP and event.button == self._LEFT:
                print "You released the left mouse button at (%d, %d)" % event.pos

        #before run
        if self._gamestate == "on your marks" and pygame.time.get_ticks() - self._timebefore >= self._interval:
            self._readysound.play()
            self._gamestate = "ready"
            self._message = "Ready"
            self._interval = 1500
            self._timebefore = pygame.time.get_ticks()
        if self._gamestate == "ready" and pygame.time.get_ticks() - self._timebefore >= self._interval:
            self._gosound.play()
            self._gamestate = "go"
            self._message = "Go"
            self._interval = 1500
            self._timebefore = pygame.time.get_ticks()
            self._racestart = self._timebefore
        if self._gamestate == "go" and pygame.time.get_ticks() - self._timebefore >= self._interval:
            self._gamestate = "run"
            self._message = ""
        if self._gamestate == 'go' or self._gamestate == 'run':
            self._racetime = pygame.time.get_ticks() - self._racestart
            self._racetimemessage = str(round(float(self._racetime)/1000,3))

        for player in self._players:
            for hurdle in self._hurdles[self._players.index(player)]:
                if player.imagelist[0].get_rect().colliderect(hurdle.image.get_rect()):
                    player.state = 'bloqued'

        for p in self._players:
            if p.x >= self._finishline - p.imagelist[0].get_width() and self._gamestate != 'win':
                self._gamestate = 'win'
                self._message = "Player " + str(self._players.index(p) + 1)  + " won"

    def _draw(self):
        #drawing
        pygame.display.flip()
        self._screen.fill((0, 0, 0))
        self._screen.blit(self._fondo, (0, 0))
        self._screen.blit(self._band, (0, 0))
        if self._message is not None:
            rendered = self._fuente.render(self._message,True,(255,255,255))
            self._screen.blit(rendered, (self._fondo.get_width() / 2 - rendered.get_width() / 2, self._band.get_height() / 2 - rendered.get_height() / 2))
        if self._racetimemessage is not None:
            rendered = self._fuente.render(self._racetimemessage,True,(255,255,255))
            self._screen.blit(rendered,(self._band.get_height() / 2 - rendered.get_height() / 2, self._band.get_height() / 2 - rendered.get_height() / 2))
        for p in self._players:
            self._screen.blit(p.currentframe(), (p.x, p.y))
        for way in self._hurdles:
            for hurdle in way:
                self._screen.blit(hurdle.image, (hurdle.x, hurdle.y))

    def restart(self):
        self.__init__()

