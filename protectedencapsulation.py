class square:
   _side = 0 #protected data member

   def __init__(self,side): #Constructor
       self._setside(side)

   def _setside(self,side): #protected member function
       self._side = side #assigning value to the protected data member

   def area(self):
       area = self._side * self._side #calculating area
       return area # returning area

side = int(input("Enter side of the square: "))
obj = square(side) # creating object and passing values to its constructor
area = obj.area() #calling area function
print("The area of the square is: ",area)
