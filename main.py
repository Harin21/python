from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid,sphere 
#using rectangle module
len=int(input("Enter the length:"))
wid=int(input("Enter the width:"))
print("Area of a rectangle=",rectangle.area(len,wid))
print("Perimeter of the rectangle=",rectangle.per(len,wid))
#using circle module
rad=int(input("Enter the radius:"))
print("Area of a circle=",circle.ar(rad))
print("Perimeter of a circle=",circle.per(rad))
#using cuboid module
len=int(input("Enter the length:"))
wid=int(input("Enter the width:"))
ht=int(input("Enter the height:"))
print("Area of a cuboid=",cuboid.sa(len,wid,ht))
print("Volume of a cuboid=",cuboid.vol(len,wid,ht))
#using sphere module
rad=int(input("Enter the radius:"))
print("Area of a sphere=",sphere.sa(rad))
print("Volume of a sphere=",sphere.vol(rad))
from figure import square,triangle
#using square module
a=int(input("Enter the side:"))
print("Area of a square=",square.area(a))
print("Perimeter of a square=",square.per(a))
#using triangle module
b=int(input("Enter the base:"))
h=int(input("Enter the height:"))
print("Area of a triangle=",triangle.area(b,h))
