import math
import matplotlib.pyplot as plt
import numpy as np

def detected(area):
    for i in range(50,80):
        for j in range(20,30):
            area[i][j]=-1
    return area
def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def neighbour_cells(posx,posy,playGround,area):
    cells=[]
    #(-1-1)
    if posx-1 >= playGround[0] and posx-1 <= playGround[1] and area[posx-1][posy-1] != -1 and posy-1 >= playGround[2] and posy-1 <= playGround[3]:
        cells.append([posx-1,posy-1])

    #(0 -1)
    if posx >= playGround[0] and posx <= playGround[1] and area[posx][posy-1] != -1 and posy-1 >= playGround[2] and posy-1 <= playGround[3]:
        cells.append([posx,posy-1])    

    #(1 -1)
    if posx+1 >= playGround[0] and posx+1 <= playGround[1] and area[posx+1][posy-1] != -1 and posy-1 >= playGround[2] and posy-1 <= playGround[3]:
        cells.append([posx+1,posy-1])  

    #(1 0)
    if posx+1 >= playGround[0] and posx+1 <= playGround[1] and area[posx+1][posy] != -1 and posy >= playGround[2] and posy <= playGround[3]:
        cells.append([posx+1,posy])

    #(1 1)
    if posx+1 >= playGround[0] and posx+1 <= playGround[1] and area[posx+1][posy+1] != -1 and posy+1 >= playGround[2] and posy+1 <= playGround[3]:
        cells.append([posx+1,posy+1])

    #(0 1)
    if posx >= playGround[0] and posx <= playGround[1] and area[posx][posy+1] != -1 and posy+1 >= playGround[2] and posy+1 <= playGround[3]:
        cells.append([posx,posy+1])
    
    #(-1 1)
    if posx-1 >= playGround[0] and posx-1 <= playGround[1] and area[posx-1][posy+1] != -1 and posy+1 >= playGround[2] and posy+1 <= playGround[3]:
        cells.append([posx-1,posy+1]) 

    #(-1 0)
    if posx-1 >= playGround[0] and posx-1 <= playGround[1] and area[posx-1][posy] != -1 and posy >= playGround[2] and posy <= playGround[3]:
        cells.append([posx-1,posy])

    return cells

#    def cost(x,y):
#   add this later when orientation aspect is added        
    def neighbour_cost(cells,posx,posy):
        cost=[]
        for i in range(0,len(cells)-1):
            for j in range(0,1):
                cost.append([])
                #i am here, working the part of finding the cost
def main():
    playGround=[0,100,0,100]
    area = [[1 for _ in range(100)] for _ in range(100)]
    """
    0: new
    1: open
    -1: obstacle
    """
    start = [0,0]
    orientation = 0
    waypoint = [[90,90],[75,80],[60,70]]
    for i in range (len(waypoint)):
        #for
        area = detected(area)
        goal = waypoint[i]
        posx = start[0]
        posy = start[1]
        cells = neighbour_cells(posx,posy,playGround,area)
    print(waypoint)
    print(cells[1][1])

if __name__=='__main__':
    main()
