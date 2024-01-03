class Rectangle:
   def __init__(self,len,breadth):
        self.breadth=breadth
        self.length=length
   def area(self):
      return(self.length*self.breadth)
   def perimeter(self):
      return(2*(self.length+self.breadth))     
print("First rectangle:")
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
rectangle1=Rectangle(length,breadth)
ar1=rectangle1.area()
print("Area of rect1=",rectangle1.area())     
print("Perimeter of rect1=",ar1) 
print("Second rectangle:")
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
rectangle2=Rectangle(length,breadth)
ar2=rectangle2.area()
print("Area of rect1=",ar2)     
print("Perimeter of rect1=",rectangle2.perimeter()) 
if(ar1>ar2):
  print("Rect1 is greater")
elif(ar2>ar1):
  print("Rect2 is greater")
else:  
   print("Both are equal")   
