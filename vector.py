import math
import numpy

class vector3:
	def __init__(self, x, y, z):
		self.v = numpy.array([x,y,z])
		
	def __repr__(self):
		return "vector3"
	
	def __str__(self):
		return str(self.v)
	
	def __add__(self, other):
		array = self.v+other.v
		return vector3(array[0], array[1], array[2])

	def __iadd__(self, other):
		self.v+=other.v
		return self

	def __sub__(self, other):
		array = self.v-other.v
		return vector3(array[0], array[1], array[2])

	def __mul__(self, mul):
		array = self.v*mul
		return vector3(array[0], array[1], array[2])

	def __truediv__(self, div):
		array = self.v/div
		return vector3(array[0], array[1], array[2])
		
	def len(self):
		return numpy.linalg.norm(self.v)

	def dot(self, other):
		return self.v.dot(other.v)
		
	def cross(self, other):
		array = numpy.cross(self.v, other.v)
		return vector3(array[0], array[1], array[2])
	
	def normalize(self):
		squaredLength = self.v[0] * self.v[0] + self.v[1] * self.v[1] + self.v[2] * self.v[2]
		if squaredLength > 0:
			invLen = 1.0 / math.sqrt(squaredLength)
			x = self.v[0] * invLen
			y = self.v[1] * invLen
			z = self.v[2] * invLen
			self.v = numpy.array([x,y,z])
		return self

class vector4:
	def __init__(self):
		self.v = numpy.array([0,0,0])
		
	def __repr__(self):
		return "vector4"
	
	def __str__(self):
		return str(self.v)
	
	def __add__(self, other):
		array = self.v+other.v
		return vector3(array[0], array[1], array[2], array[3])

	def __iadd__(self, other):
		self.v+=other.v
		return self

	def __sub__(self, other):
		array = self.v-other.v
		return vector3(array[0], array[1], array[2], array[3])

	def __mul__(self, mul):
		array = self.v*mul
		return vector3(array[0], array[1], array[2], array[3])

	def __truediv__(self, div):
		array = self.v/div
		return vector3(array[0], array[1], array[2], array[3])
		
	def len(self):
		return numpy.linalg.norm(self.v)

	def dot(self, other):
		return self.v.dot(other.v)
		
	def normalize(self):
		squaredLength = self.v[0] * self.v[0] + self.v[1] * self.v[1] + self.v[2] * self.v[2] + self.v[3] * self.v[3]
		if squaredLength > 0:
			invLen = 1.0 / math.sqrt(squaredLength)
			x = self.v[0] * invLen
			y = self.v[1] * invLen
			z = self.v[2] * invLen
			w = self.v[3] * invLen
			self.v = numpy.array([x,y,z,w])
		return self
		
	@classmethod
	def FromValue(cls, x, y, z, w):
		v4 = cls()
		v4.v = numpy.array([x, y, z, w])
		return v4

	@classmethod
	def FromVector3(cls, v3):
		v4 = cls()
		v4.v = numpy.array([v3.v[0], v3.v[1], v3.v[2], 0])
		return v4
		
'''		
v1 = vector3(2,3,4)
v2 = vector3(4,5,6)

#print(v1)
#v1 += v2
#print(v1)

x = v1.normalize()
print(v1)
z = x.cross(v2).normalize()
y = z.cross(x).normalize()

print(x)
print(y)
y.normalize()
print(z)

#print(v1-v2)
#print(math.sqrt(v1.dot(v1)))
#print(v1.cross(v2))
#print(v1.len())

#print(x.dot(y))
#print(x.dot(z))
#print(y.dot(z))
'''

'''
class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Lines")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  
'''