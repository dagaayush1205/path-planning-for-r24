import math
import matplotlib.pyplot as plt
import numpy as np

def detected(area):
    for i in range(0,2500):
        for j in range(10,250):
            area[i][j]=-1

    return area
def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def neighbour_cells(pos,playGround,area,orientation_last):
    cells=[]
    orientation=[]
    print(orientation_last)
    #(-1-1)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]-1][pos[1]-1] != -1:
            cells.append([pos[0]-1,pos[1]-1])
            if(math.fabs(orientation_last-225)>=180):
                orientation.append([math.fabs(225-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-225)])

    #(0 -1)
    if pos[0] >= playGround[0] and pos[0] <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]][pos[1]-1] != -1:
            cells.append([pos[0],pos[1]-1]) 
            if(math.fabs(orientation_last-270)>=180):
                orientation.append([math.fabs(270-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-270)])

    #(1 -1)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]+1][pos[1]-1] != -1:
            cells.append([pos[0]+1,pos[1]-1])  
            if(math.fabs(orientation_last-315)>=180):
                orientation.append([math.fabs(315-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-315)])
    #(1 0)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        if area[pos[0]+1][pos[1]] != -1:
            cells.append([pos[0]+1,pos[1]])
            if(math.fabs(orientation_last-360)>=180):
                orientation.append([math.fabs(360-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-360)])

    #(1 1)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]+1][pos[1]+1] != -1:
            cells.append([pos[0]+1,pos[1]+1])
            if(math.fabs(orientation_last-180)>=180):
                orientation.append([math.fabs(45-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-45)])

    #(0 1)
    if pos[0] >= playGround[0] and pos[0] <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]][pos[1]+1] != -1:
            cells.append([pos[0],pos[1]+1])
            if(math.fabs(orientation_last-90)>=180):
                orientation.append([math.fabs(90-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-90)])
    
    #(-1 1)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]-1][pos[1]+1] != -1:
            cells.append([pos[0]-1,pos[1]+1]) 
            if(math.fabs(orientation_last-135)>=180):
                orientation.append([math.fabs(135-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-135)])

    #(-1 0)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        if area[pos[0]-1][pos[1]] != -1:
            cells.append([pos[0]-1,pos[1]])
            if(math.fabs(orientation_last-180)>=180):
                orientation.append([math.fabs(180-orientation_last)])
            else:
                orientation.append([math.fabs(orientation_last-180)])
    print(cells)
    return cells,orientation
       
def neighbour_least_cost(cells,pos,goal,orientation):
    cost=[]
    least=[0,0,100000,0]
    for i in range(0,len(cells)-1):
        a = distance(cells[i][0],cells[i][1],pos[0],pos[1])+distance(cells[i][0],cells[i][1],goal[0],goal[1])
        cost.append([cells[i][0],cells[i][1],a])
        if least[2] > cost[i][2]:
            least[0] = cost[i][0]
            least[1] = cost[i][1]
            least[2] = cost[i][2]
            least[3] = orientation[i]
            print(orientation[i])
        print("Cost:",cost)
        print("least:",least)
    #plt.plot([pos[0],pos[1]],[least[0],least[1]],"-b")
    print("final:",least)
    return least

def main():
    playGround=[0,10000,0,400]
    area = [[1 for _ in range(playGround[3])] for _ in range(playGround[1])]
    print(area)
    """
    0: new
    1: open
    -1: obstacle
    """
    
    start = [1,1]
    orientation_last = 0
    waypoint = [[300,300]]
    #goal = waypoint[1]
    plt.axis([0,10000,0,500])
    for i in range (len(waypoint)):
        goal = waypoint[i]
        print(i)
        pos = start
        while pos != goal:
            area = detected(area)
            plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])
            ab, orientation = neighbour_cells(pos,playGround,area,orientation_last)
            a = neighbour_least_cost(ab,pos,goal,orientation)
            plt.pause(0.0001)
            plt.plot(goal[0], goal[1], "-xr")
            plt.plot(pos[0],pos[1],"-xg")
            plt.plot([0,10000,10000,0,0],[0,0,400,400,0],"-r")
            pos[0]=a[0]
            pos[1]=a[1]
            orientation_last=float(a[3])
            print("next step:",a)
        print("ALERT: Reached Waypoint",i)
    plt.show()
        



if __name__=='__main__':
    main()
