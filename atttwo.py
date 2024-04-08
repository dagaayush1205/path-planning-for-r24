import math
import matplotlib.pyplot as plt
import numpy as np


def detected(area):
    for i in range(50,80):
        for j in range(20,30):
            area[i,j,0]=-1

def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def neighbour(posx,posy,playGround):
    #over here, i was write every condition for all the 9 grids check notebook for more hints
    if posx-1>=playGround[0] and posx-1<=playGround[1] and posx-1
    cells=[[]]

def neighbour_cost(x,y):
    if x1-1

def main():
    playGround=[0,100,0,100]
    area = np.full((playGround[1],playGround[3],1),1)
    """
    0: new
    1: open
    -1: obstacle
    """
    start = [0,0]
    waypoint = [[90,90],[75,80],[60,70]]
    for i in range (len(waypoint)):
        area = detected(area)
        goal = waypoint[i]
        posx = start[0]
        posy = start[1]


    print(len(waypoint))
if __name__=='__main__':
    main()
