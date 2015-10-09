import Image
import numpy as np
import math
class to8bit:
	def __init__(self,n=4):
		self.blocksize = n
	def loadImg(self, imgpath):
		self.img = Image.open(imgpath)
	def toArray(self):
		self.imgarray = np.asarray(self.img)
		self.imgarray.setflags(write=True)
		if len(self.imgarray.shape) == 3:
			self.r = self.imgarray.shape[0]
			self.c = self.imgarray.shape[1]
			self.channel = 3
		else:
			pass
	def pad(self):
		r_factor = math.ceil(self.r / float(self.blocksize))
		c_factor = math.ceil(self.c / float(self.blocksize))
		pad_img = np.zeros([r_factor*self.blocksize, c_factor*self.blocksize, self.channel])
		pad_img[0:self.r, 0:self.c, :] = self.imgarray[:,:,:]
		self.imgarray = pad_img