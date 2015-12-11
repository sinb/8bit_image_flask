#!/usr/bin/env python
# coding=utf-8
import sys
from to8bit import *
from palette import *

image_file = sys.argv[1]

preset = Palette()
pic = to8bit()

pic.loadImg(image_file)
palette = preset('SuperMarioBros')
## 还有其他风格!
# print palette.preset.keys()


img = pic.pixelize(palette, 8) ## 第二个参数可选择粒度,越小越慢
img.save('asdf.jpg')
