import math
import matplotlib.pyplot as plt
import numpy as np

def detected(area):
    for i in range(50,80):
        for j in range(50,80):
            area[i][j]=-1
    area[1][1]=-1
    return area
def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def neighbour_cells(pos,playGround,area):
    cells=[]
    #(-1-1)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and area[pos[0]-1][pos[1]-1] != -1 and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        cells.append([pos[0]-1,pos[1]-1])

    #(0 -1)
    if pos[0] >= playGround[0] and pos[0] <= playGround[1] and area[pos[0]][pos[1]-1] != -1 and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        cells.append([pos[0],pos[1]-1])    

    #(1 -1)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and area[pos[0]+1][pos[1]-1] != -1 and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        cells.append([pos[0]+1,pos[1]-1])  

    #(1 0)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and area[pos[0]+1][pos[1]] != -1 and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        cells.append([pos[0]+1,pos[1]])

    #(1 1)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and area[pos[0]+1][pos[1]+1] != -1 and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        cells.append([pos[0]+1,pos[1]+1])

    #(0 1)
    if pos[0] >= playGround[0] and pos[0] <= playGround[1] and area[pos[0]][pos[1]+1] != -1 and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        cells.append([pos[0],pos[1]+1])
    
    #(-1 1)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and area[pos[0]-1][pos[1]+1] != -1 and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        cells.append([pos[0]-1,pos[1]+1]) 

    #(-1 0)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and area[pos[0]-1][pos[1]] != -1 and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        cells.append([pos[0]-1,pos[1]])

    return cells

#    def cost(x,y):
#   add this later when orientation aspect is added        
def neighbour_least_cost(cells,pos,goal):
    cost=[]
    least=[10,10,100000]
    for i in range(0,len(cells)-1):
        a = distance(cells[i][0],cells[i][1],pos[0],pos[1])+distance(cells[i][0],cells[i][1],goal[0],goal[1])
        cost.append([cells[i][0],cells[i][1],a])
        if least[2] >= cost[i][2]:
            least[0] = cost[i][0]
            least[1] = cost[i][1]
            least[2] = cost[i][2]
    return least

def main():
    playGround=[0,10000,0,400]
    area = [[1 for _ in range(playGround[1])] for _ in range(playGround[3])]
    """
    0: new
    1: open
    -1: obstacle
    """
    start = [0,0]
    orientation = 0
    waypoint = [[90,90],[75,80],[600,60]]
    for i in range (len(waypoint)):
        #for
        area = detected(area)
        goal = waypoint[i]
        pos = start
        while pos != goal:
            a = neighbour_least_cost(neighbour_cells(pos,playGround,area),pos,goal)
            pos[0]=a[0]
            pos[1]=a[1]
            print(a)
        print("ALERT: Reached ",i)

if __name__=='__main__':
    main()
