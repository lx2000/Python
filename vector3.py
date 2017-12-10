import math
import numpy

class vector3:
	v = numpy.array([0,0,0])
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
		return self / self.len()

'''		
v1 = vector3(2,3,4)
v2 = vector3(4,5,6)

print(v1)
v1 += v2
print(v1)

x = v1.normalize()
z = x.cross(v2).normalize()
y = z.cross(x).normalize()

print(x)
print(y)
#y.normalize()
print(z)

#print(v1-v2)
#print(math.sqrt(v1.dot(v1)))
#print(v1.cross(v2))
#print(v1.len())

print(x.dot(y))
print(x.dot(z))
print(y.dot(z))
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