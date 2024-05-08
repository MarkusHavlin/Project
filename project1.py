#Author: 
#Project Name: 
#Date Created: 
#Description: 
#             

import math

def quadrant_check(x, y): #TODO
    if int(x) > 0 and int(y) > 0:
        print("This point is in Quadrant I")
    elif int(x) < 0 and int(y) > 0:
        print("This point is in Quadrant II")
    elif int(x) < 0 and int(y) < 0:
        print("This point is in Quadrant III")
    elif int(x) > 0 and int(y) < 0:
        print("This point is in Quadrant IV")
    elif int(x) == 0 and int(y) == 0:
        print("This point is on the origin")
    elif int(x) == 0:
        print("This point is on the x-axis")
    elif int(y) == 0:
        print("This point is on the y-axis")

def find_distance(x, y): #TODO
    distance = math.sqrt((int(x)**2) + (int(y)**2))
    return distance

def cont():
    answer = input("Would you like to continue? (y/n) ")
    
    if answer == "y":
        main()
    elif answer == "n":
        exit()
    else:
        print("Error: The user did not enter 'y' or 'n' ")
        cont()

def main():
     
    
    x = input("x value: ")
    y = input("y value: ")
    coordinate = (x, y)

    
    print("The point is ",coordinate, quadrant_check(x, y)) #Uses the return value of quadrant_check() to print the quadrant
    
    print("The distance from the origin is: ", find_distance(x, y)) #Uses the return of find_distance to print the distance from origin
    
    cont() #Calls the cont() function to see if the user would like to continue continue the program or end


main() #Only function call. DO NOT CHANGE THIS
