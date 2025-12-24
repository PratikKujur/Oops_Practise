"""
Define a circle class to create a circle with radius r using the constructor
Define area and perimeter 
"""

class circle:
    def __init__(self,r):
        self.r=r


    def perimeter(self):
        print(f"Perimeter iof circle {self.r} is",2*3.14*self.r)

    def area(self):
        print(f"Area of circle with radius {self.r} is",3.14*self.r**2)


c1=circle(r=10)
print(c1.perimeter())
print(c1.area())        