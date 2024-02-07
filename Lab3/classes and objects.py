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
