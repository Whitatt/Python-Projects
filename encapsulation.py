class rectangle:
   __length = 0 #private data member
   __breadth = 0 #private data member

   def __init__(self,len,bre): #Constructor
       self.__setlenght(len)
       self.__setbreadth(bre)

   def __setlenght(self,len): #private member function
       self.__length = len #assigning value to the private data member

   def __setbreadth(self,bre): #private member function
       self.__breadth = bre #assigning value to the private data member

   def area(self):
       area = self.__length * self.__breadth #calculating area
       return area # returning area

len = int(input("Enter length: ")) #Accepting data from user
bre = int(input("Enter Breadth: ")) #Accepting data from user
obj = rectangle(len,bre) # creating object and passing values to its constructor
area = obj.area() #calling area function
print("The area of the rectangle is: ",area)
obj.__setlength() #this function in not accessible
obj.__setbreadth() #this function in not accessibl



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
