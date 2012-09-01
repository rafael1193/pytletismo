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

class Credits:

    def __init__(self):
        self._mousepos = (0, 0)
        self._LEFT = 1
        self._fuente = pygame.font.SysFont('sans', 16, False, False)
        self._fuentetitle = pygame.font.SysFont('sans', 18, True, False)
        self._running = True
        self._title = "Pytletismo"
        self._copyright = u"Copyright (C) 2012 Rafael Bailón-Ruiz"
        self._license = ["This program is free software: you can redistribute it and/or modify", \
        "it under the terms of the GNU General Public License as published by", \
        "the Free Software Foundation, either version 3 of the License, or", \
        "(at your option) any later version.", \
        "", \
        "This program is distributed in the hope that it will be useful,", \
        "but WITHOUT ANY WARRANTY; without even the implied warranty of", \
        "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the", \
        "GNU General Public License for more details.", \
        "", \
        "You should have received a copy of the GNU General Public License", \
        "along with this program.  If not, see <http://www.gnu.org/licenses/>.", \
        "", \
        "", \
        "Pictures, sounds and scripts are licensed under a ", \
        u"Creative Commons Reconocimiento 3.0 España License."]
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
                pressedkeys = pygame.key.get_pressed()
                if pressedkeys[pygame.K_ESCAPE] or pressedkeys[pygame.K_RETURN]:
                    self._running = False
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self._LEFT:
                pass
            elif event.type == pygame.MOUSEBUTTONUP and event.button == self._LEFT:
                print "You released the left mouse button at (%d, %d)" % event.pos

    def _draw(self):
        #drawing
        pygame.display.flip()
        self._screen.fill((0, 0, 0))
        if self._title is not None:
            rendered = self._fuentetitle.render(self._title,True,(255,255,255), (0,0,0))
            self._screen.blit(rendered, (self._screen.get_width() / 2 - rendered.get_width() / 2, 90))
        if self._copyright is not None:
            rendered = self._fuente.render(self._copyright,True,(255,255,255), (0,0,0))
            self._screen.blit(rendered, (self._screen.get_width() / 2 - rendered.get_width() / 2, 130))
        if self._license is not None:
            i = 0
            for line in self._license:
                rendered = self._fuente.render(line,True,(255,255,255), (0,0,0))
                self._screen.blit(rendered,(self._screen.get_width() / 2 - rendered.get_width() / 2, 170 + 17 * i))
                i += 1

