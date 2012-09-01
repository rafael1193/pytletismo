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

import player
import math
import random

class Jumper(player.Player):

    def __init__(self, imagelist, posX, posY, speed, keylist):
        super(Jumper, self).__init__(imagelist, posX, posY, speed, keylist)
        self.state = 'running'
        self._y0 = self.y

    def update(self, time):
        if self.state == 'running':
            if self.speed != 0:
                self.x += self.speed + random.randrange(0, 3) * random.random()
        elif self.state == 'stopping':
            self.speed -= 0.1
            if self.speed <=0:
                self.speed = 0
                self.state = 'stopped'
            self.x += self.speed
        elif self.state == 'jumping':
            self.speed += random.randrange(0, 1) * random.random()
            self.x = self.x + math.sin(45) * 1.5 * self.speed
            self.y = self.y - math.sin(45) *self.speed * time/10 + 0.5 * 3 * (time/10) ** 2
            #print "jump " + str((time, self.x, self.y))
            if self.y >= self._y0:
                self.state = 'landed'
                #print "landed!"
        elif self.state == 'stopped' or self.state == 'end':
            pass
        return
