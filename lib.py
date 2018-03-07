#!/usr/bin/python3

	#x y
	#z w
#x y  
#z w   @
class Matrix:
	def __init__(self, x, y, z, w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
	def add(self, m):
		return Matrix(self.x + m.x,self.y + m.y,self.z + m.z,self.w + m.w)
	def product(self, m):
		x = self.x * m.x + self.y * m.z;
		y = self.x * m.y + self.y * m.w;
		z = self.z * m.x + self.w * m.z;
		w = self.z * m.y + self.w * m.w; 
		return Matrix(x,y,z,w)

