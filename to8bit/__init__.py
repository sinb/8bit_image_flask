import Image
import numpy as np
import math
import sys
class to8bit:
    def __init__(self):
        pass
    def loadImg(self, imgpath):
        self.img = Image.open(imgpath) #image object
        self.imgarray = np.asarray(self.img) # to array
        self.imgarray.setflags(write=True)
        if len(self.imgarray.shape) == 3:
            self.r = self.imgarray.shape[0]
            self.c = self.imgarray.shape[1]
            self.channel = 3
        else:
            pass
    def _pad(self, blocksize):
        r_factor = math.ceil(self.r / float(blocksize))
        c_factor = math.ceil(self.c / float(blocksize))
        pad_img = np.zeros([int(r_factor*blocksize), int(c_factor*blocksize), self.channel], dtype=np.uint8)
        pad_img[0:self.r, 0:self.c, ...] = self.imgarray[...]
        self.imgarray = pad_img

    def getClosestColor(self, color, palette):
        min_dist = sys.maxint
        min_idx = 0
        for i in range(len(palette)):
            dist = np.sqrt(np.sum(np.abs(color-palette[i, :]))**2)
            if dist < min_dist:
                min_dist = dist
                min_idx = i
        return min_idx
        
    def getMeanColor(self, block, blocksize):
        r = block[:,:,0].sum() / float(blocksize**2)
        g = block[:,:,1].sum() / float(blocksize**2)
        b = block[:,:,2].sum() / float(blocksize**2)
        return [r, g, b]
        
    def pixelize(self, palette, blocksize=8):
        self._pad(blocksize)
        row = 0
        while row < self.imgarray.shape[0]:
            col = 0
            while col < self.imgarray.shape[1]:
                meanColor = self.getMeanColor(self.imgarray[row:row+blocksize, col:col+blocksize,:], blocksize)
                idx = self.getClosestColor(meanColor, palette)
                self.imgarray[row:row+blocksize-1, col:col+blocksize-1,:] = palette[idx]
                col += blocksize
            row +=blocksize
        self.imgarray = self.imgarray[0:self.r, 0:self.c, :]   
        return Image.fromarray(self.imgarray, 'RGB')

