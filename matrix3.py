import math
import numpy
from vector3 import vector3

class matrix3:
	x = vector3(1,0,0)
	y = vector3(0,1,0)
	z = vector3(0,0,1)

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return "matrix3"
	
	def __str__(self):
		array = numpy.array([self.x.v, self.y.v, self.z.v])
		return str(array)
		
	def __add__(self, other):
		return matrix3(self.x+other.x, self.y+other.y, self.z+other.z)
		
	def __sub__(self, other):
		return matrix3(self.x-other.x, self.y-other.y, self.z-other.z)

	def __mul__(self, other):
		arrayself = numpy.array([self.x.v, self.y.v, self.z.v])
		arrayother = numpy.array([other.x.v, other.y.v, other.z.v])
		arrayret = arrayself.dot(arrayother)
		vx = vector3(arrayret[0][0], arrayret[0][1], arrayret[0][2])
		vy = vector3(arrayret[1][0], arrayret[1][1], arrayret[1][2])
		vz = vector3(arrayret[2][0], arrayret[2][1], arrayret[2][2])
		return matrix3(vx, vy, vz)
		#return matrix3(self.x-other.x, self.y-other.y, self.z-other.z)
		
	def inverse(self):
		array = numpy.array([self.x.v, self.y.v, self.z.v])
		inv = numpy.linalg.inv(array)
		return inv
		
x = vector3(12,44,5)
y = vector3(1,4,9)
z = vector3(12,4,57)

#x += y
#print(x*y)

m1 = matrix3(x,y,z)
print(m1)
print("*")
#print(m1.inverse())
m2 = matrix3(y,y,y)
print(m2)
print("=")
print(m1*m2)
print(m2*m1)
#print(m1)
#print(m1)
#print(m1+m2)
	#matrix3