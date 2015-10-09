#!/usr/bin/env python
# coding=utf-8
from to8bit import *
from palette import *
preset = Palette()
pic = to8bit()

pic.loadImg('uploads/hope6.jpg')
palette = preset('NES')
img = pic.pixelize(palette, 8)
img.save('adsd.jpg')
# img = Image.fromarray(pic.imgarray , 'RGB')