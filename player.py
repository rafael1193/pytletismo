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
import random

class Player(pygame.sprite.Sprite):
    """Sprite representing a player"""
    def __init__(self, imagelist, posX, posY, speed, keylist):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.x = posX
        self.y = posY
        self.speed = speed
        self.imagelist = imagelist
        self.keys = keylist
        self._imageindex=0
        self.bloqued = False

    def update(self):
        if not self.bloqued:
            self.x += self.speed + random.randrange(0, 3) * random.random()
        return

    def nextframe(self):
        if self._imageindex < len(self.imagelist) - 1:
            self._imageindex += 1
        else:
            self._imageindex = 0
        return self.imagelist[self._imageindex]

    def currentframe(self):
        return self.imagelist[self._imageindex]
