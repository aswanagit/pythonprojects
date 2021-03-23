class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
r1=Rectangle(4,5)
r2=Rectangle(7,8)
print("rectangle1 area:",r1.area())
print("rectangle2 area:",r2.area())
if(r1.area()>r2.area()):
    print("area of rectangle1 is greater")
else:
    print("area of rectangle2 is greater")
print("rectangle1 perimeter:",r1.perimeter())
print("rectangle2 perimeter:",r2.perimeter())
