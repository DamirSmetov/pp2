class My_shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def __str__(self):
        return f"The object is filled by {self.color}. This statement is {self.is_filled}"
    def getArea(self):
        return 0
    
x = My_shape("green", True)
print(x)
class Rectangle(My_shape):
    def __init__(self, x_top_left, y_top_left, length, width):
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width
    def __str__(self):
        return f"x_top left : {self.x_top_left}. y_top_left : {self.y_top_left}. length : {self.length}. width : {self.width}"
    def getArea(self):
        return self.length * self.width    
class Circle(My_shape):
    def __init__(self, x_center, y_center, radius):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    def __str__(self):
        return f"x_center : {self.x_center}. y_center : {self.y_center}. radius : {self.radius}"
    def getArea (self):
        return 3.14 * self.radius **2
a = Rectangle(int(input("x_top_left :")), int(input("y_top_left : ")), int(input("Length : ")), int(input("Width : ")))
print(a)
print(a.getArea())
b = Circle(int(input("x_center : ")), int(input("y_center : ")), int(input("radius : ")))
print(b)
print(b.getArea())
    

            
