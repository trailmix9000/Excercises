"""
In this excercise I create 3 classes Circle(), Rectangle(), 
and Point().
pointInCircle() determines if a point lies in the circle.
RectInCircle() determines if all corners of the rectangle lie within the circle. 
RectCircleOverlap() determines if only one corner lies in the circle. 
"""
import math
import turtle


class Circle:
    def __init__(self, centerX, centerY, radius):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius

        
class Rectangle:
    def __init__(self, x, y, width, height): 
        self.corner = Point(x, y)
        self.width = width
        self.height = height

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pointInCircle(point, circle): #tells whether a point lies in the circle
        distance = math.sqrt((point.x - circle.centerX) ** 2 + (point.y - circle.centerY) ** 2)
        if distance <= circle.radius:
            return True
        else:
            return False
        

def rectInCircle(rectangle, circle):
    # Calculate the coordinates of the rectangle's four corners
    x1 = rectangle.corner.x
    y1 = rectangle.corner.y
    x2 = rectangle.corner.x + rectangle.width
    y2 = rectangle.corner.y
    x3 = rectangle.corner.x + rectangle.width
    y3 = rectangle.corner.y + rectangle.height
    x4 = rectangle.corner.x
    y4 = rectangle.corner.y + rectangle.height

    # Check if all four corners of the rectangle lie within or on the circle
    if (
        (x1 - circle.centerX) ** 2 + (y1 - circle.centerY) ** 2 <= circle.radius ** 2 and
        (x2 - circle.centerX) ** 2 + (y2 - circle.centerY) ** 2 <= circle.radius ** 2 and
        (x3 - circle.centerX) ** 2 + (y3 - circle.centerY) ** 2 <= circle.radius ** 2 and
        (x4 - circle.centerX) ** 2 + (y4 - circle.centerY) ** 2 <= circle.radius ** 2
    ):
        return True
    else:
        return False
    

def rectCircleOverlap(rectangle, circle):
    # Calculate the coordinates of the rectangle's four corners
    x1 = rectangle.corner.x
    y1 = rectangle.corner.y
    x2 = rectangle.corner.x + rectangle.width
    y2 = rectangle.corner.y
    x3 = rectangle.corner.x + rectangle.width
    y3 = rectangle.corner.y + rectangle.height
    x4 = rectangle.corner.x
    y4 = rectangle.corner.y + rectangle.height
    # Check if all four corners of the rectangle lie within or on the circle
    if (
        (x1 - circle.centerX) ** 2 + (y1 - circle.centerY) ** 2 <= circle.radius ** 2 or
        (x2 - circle.centerX) ** 2 + (y2 - circle.centerY) ** 2 <= circle.radius ** 2 or
        (x3 - circle.centerX) ** 2 + (y3 - circle.centerY) ** 2 <= circle.radius ** 2 or
        (x4 - circle.centerX) ** 2 + (y4 - circle.centerY) ** 2 <= circle.radius ** 2
    ):
        return True
    else:
        return False
    

if __name__ == "__main__":
    # Some testing
    myCircle = Circle(0,0,5)
    myPoint = Point(1,2)
    myRectangle = Rectangle(0,0,1,1)
    print(pointInCircle(myPoint, myCircle))
