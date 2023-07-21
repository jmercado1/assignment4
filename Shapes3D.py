import math

square = {
    'width': 5,
    'height': 5,
}

rectangle = {
    'width': 5,
    'height': 8,
    'color': 'red',
}


def bar(this, that):
            return this + that


foo = Rectangle(5, 8)
foo.width



class Shape():
     def __init__(self):
          raise NotImplementedError
     def getPerimeter(self):
          raise NotImplementedError
     def getArea(self):

class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    def getPerimeter(self):
          return (self.width * 2) + (self.height * 2)
    def getArea (self):
          return self.width * self.height
    
    foo = Rectangle(4, 5)
    foo.getArea()


from Shapes3D import Circle
import Shapes3D import Polygon
    
class Cylinder():
    def __init__(self, radius, height):
         self.base = Circle(radius=radius)
         self.height = height
    def getSurfaceArea(self):
         (self.base.getArea () * 2) + (self.base.getPerimeter () * self.height)
         def getVolume(self):
              self.base.getArea() * self.height
    



class Dog():
         def __init__ (self, name, color):
              self.name = name
              self.color = color
         def bark(self):
            print ('BARK!')
         def shake(self):
              print('''
              \/\/\/
              ''')

class ShowDog():
     def __init__(self, name, color, grade):
          super().__init__(name, color)
          self.grade = grade
     def laydown(self):
          print('________')

riker = Dog('riker', 'brown')
riker.laydown()
milo.laydown()  
milo.grade

milo = ShowDog('milo', 'white')
 