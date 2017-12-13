import math
import numpy
from matrix3 import matrix3
from vector import vector3, vector4

class matrix4:
	def __init__(self):
		self.x = vector4()
		self.y = vector4()
		self.z = vector4()
		self.pos = vector4()

	def __repr__(self):
		return "matrix4"
	
	def __str__(self):
		array = numpy.array([self.x.v, self.y.v, self.z.v, self.pos.v])
		return str(array)
		
	def __add__(self, other):
		return matrix4(self.x+other.x, self.y+other.y, self.z+other.z, self.pos+other.pos)
		
	def __sub__(self, other):
		return matrix3(self.x-other.x, self.y-other.y, self.z-other.z)

	def __mul__(self, other):
		arrayself = numpy.array([self.x.v, self.y.v, self.z.v, self.pos.v])
		arrayother = numpy.array([other.x.v, other.y.v, other.z.v, other.pos.v])
		arrayret = arrayself.dot(arrayother)
		return matrix4.FromArray(arrayret)

	def inverse(self):
		array = numpy.array([self.x.v, self.y.v, self.z.v, self.pos.v])
		inv = numpy.linalg.inv(array)
		return matrix4.FromArray(inv)
		
	@classmethod
	def Identity(cls):
		x = vector4.FromValue(1, 0, 0, 0)
		y = vector4.FromValue(0, 1, 0, 0)
		z = vector4.FromValue(0, 0, 1, 0)
		pos = vector4.FromValue(0, 0, 0, 1)
		return matrix4.FromValue(x, y, z, pos)
	
	@classmethod
	def FromArray(cls, array):
		mat = cls()
		mat.x = vector4.FromValue(array[0][0], array[0][1], array[0][2], array[0][3])
		mat.y = vector4.FromValue(array[1][0], array[1][1], array[1][2], array[1][3])
		mat.z = vector4.FromValue(array[2][0], array[2][1], array[2][2], array[2][3])
		mat.pos = vector4.FromValue(array[3][0], array[3][1], array[3][2], array[3][3])
		return mat

	@classmethod
	def FromValue(cls, x, y, z, pos):
		mat = cls()
		mat.x = x
		mat.y = y
		mat.z = z
		mat.pos = pos
		return mat
		
	@classmethod
	def FromRotAndPos(cls, m, pos):
		mat = cls()
		mat.x = vector4.FromVector3(m.x)
		mat.y = vector4.FromVector3(m.y)
		mat.z = vector4.FromVector3(m.z)
		mat.pos = vector4.FromVector3(pos)
		mat.pos.v[3] = 1
		return mat

forward = vector3(7.10119629,-25.3019409,-23.1168213)
up = vector3(0.726603448,-0.341014385,0.596453547)
pos = vector3(1,2,3)
m1 = matrix3.Identity()
print(m1)
mat = matrix3.MakeLookAt(forward, up)
print(mat)

#x4 = vector4.FromVector3(m1.x)
#y4 = vector4.FromVector3(m1.y)
#y4 = vector4.FromVector3(m1.z)
m4 = matrix4.FromRotAndPos(mat, pos)
print(m4)
inv = m4.inverse()
print(inv)
print(inv*m4)
print(m4*inv)


'''
#print(m1)
#print(m1)
#print(m1+m2)
	#matrix3
'''