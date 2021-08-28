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



