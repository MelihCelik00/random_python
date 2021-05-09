#!/usr/bin/env python

import numpy as np
from scipy.spatial import ConvexHull

def PolyArea2D(pts):
    lines = np.hstack([pts,np.roll(pts,-1,axis=0)])
    area = 0.5*abs(sum(x1*y2-x2*y1 for x1,y1,x2,y2 in lines))
    return area

isQuitTrue = False
pointList = []

print("Program to Calculate Convex Hull Area")

while(isQuitTrue==False):
    myInput = input("Press 'c' To Enter Coordinates or Press 'q' To Exit: ")
    
    if(myInput=="q" or myInput=="Q"):
        isQuitTrue = True
        break

    elif(myInput=="c" or myInput=="C"):
        xCoordinate = int(input("Enter x coordinate: "))
        yCoordinate = int(input("Enter y coordinate: "))
        pointList.append([xCoordinate,yCoordinate])

        continueInput = input("To continue adding points precc 'c', to calculate area press 'a': ")
        if(continueInput=="c" or continueInput =="C"):
            continue
        elif(myInput=="a" or myInput=="A"):
            isQuitTrue = True
    else:
        print("Invalid input try again\n")
        
print("Your list of points: ",pointList)
print("Area: ", PolyArea2D(pointList))

points = np.array([(1, 2), (3, 4), (3, 6), (2, 4.5), (2.5, 5)])
hull = ConvexHull(pointList)

np.random.seed(1)
random_points = np.random.uniform(0, 6, (100, 2))
#print("randpoints: ",random_points)

# get array of boolean values indicating in hull if True
in_hull = np.all(np.add(np.dot(random_points, hull.equations[:,:-1].T),
                        hull.equations[:,-1]) <= 0.5, axis=1)

random_points_in_hull = random_points[in_hull]

#print(random_points_in_hull)

howManyNumInHull = 0

for i in range(len(random_points_in_hull)):
    howManyNumInHull+=1
print("What percent is in this area: ",howManyNumInHull/100)