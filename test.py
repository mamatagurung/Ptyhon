
# for number in range(1, 100):
#     if number % 5 == 0:
#         print(number)
       

# for char_code in range(ord('a'), ord('z')+1, 2):
#     char = chr(char_code)
#     print(char)

num = {1,2,3,4,5}

for num in range(5):
    print(num)


d ={'A' :1, 'B':[3,4], 'C':[1,2,3]}

d['B'][0] =4
print(d)


a = 5
if a > 5 : 
    print("gwello")
    print("number is greater" )
elif a>=5:
    print("exception")
else: 
    print("less than or equal to 5")
 
x, y = 10, 20

maxval = x if x > y else y
print(maxval)

myList =[1,2,3,4,5]

for item in myList:
    print("No is", item)

x = 0
while x < 5:
    x += 1
print("done")

# functions
def add(a,b):
    return (a + b)


add(3,5)

# Object oriented programming(oop)
class Rectangle: 
    def __init__(self, length=0, breadth=0):
     self.length = length 
     self.breadth = breadth
     def area(self):
       self.area = length * breadth
       return self.area

r1 = Rectangle(3,4)
r1.length = 5
r1.area()
# numpy, matplotlib panda

# import numpy as np
# np.array([1,2,3,4])

# stack queue tree
# data inserting and accessing

# depth first search and breadth first search