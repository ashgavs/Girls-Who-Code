
#QUESTION 1, possible solution a
def rootBeersOnTheWall(number):
    if number == 1:
        print("1 bottle of root beer on the wall, 1 bottle of root beer. Take it down, pass it around, 0 bottles of root beer on the wall.")
    elif number == 2:
        print("2 bottles of root beer on the wall, 2 bottles of root beer. Take one down, pass it around, 1 bottle of root beer on the wall.")
    else:
         print(number, " bottles of root beer on the wall, ", number, "bottles of root beer. Take one down, pass it around, ", number-1, " bottles of root beer on the wall.")
        
              
#QUESTION 1, possible solution b
def rootBeersOnTheWall2(number):
    if number == 1:
        bottles = "bottle"
        bottlesMinus1 = "bottles"
    elif number == 2:
        bottles = "bottles"
        bottlesMinus1 = "bottle"
    else:
        bottles = "bottles"
        bottlesMinus1 = "bottles"
    print(number, bottles, " of root beer on the wall, ", number, bottles, " of root beer. Take one down, pass it around, ", number-1, bottlesMinus1, " of root beer on the wall.")
    

rootBeersOnTheWall(2)
rootBeersOnTheWall2(4)


#Question 2, possible solution a
n = 99
while n > 0:
    rootBeersOnTheWall(n)
    n = n - 1
    
#Question 2, possible solution b
n = 99 
for i in range(n):
    rootBeersOnTheWall(n)
    n = n - 1
    
#Question 2, possible solution c
def recursiveWay(n):
    if n == 0:
        return 
    else:
        rootBeersOnTheWall(n)
        recursiveWay(n-1)
    
recursiveWay(3)
    
