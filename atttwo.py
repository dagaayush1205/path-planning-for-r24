import math
import matplotlib.pyplot as plt
import numpy as np

def group_set(area, x1, x2):
    for i in range(min(x1[0], x2[0]), max(x1[0], x2[0])):
        for j in range(min(x1[1], x2[1]), max(x1[1], x2[1])):
            area[i][j] = -1

    obs_plot(x1[0],x1[1],x2[0],x2[1])
def obs_plot(x1,y1,x2,y2):
    # plt.plot([x1,x2],[y1,y2],"-b")#12
    # plt.plot([x2,x2],[y1,y2],"-b")#23
    # plt.plot([x2,x1],[y2,y2],"-b")#34
    # plt.plot([x1,x1],[y2,y1],"-b")#45
    # plt.show()
    a = sorted([x1, x2])
    b = sorted([y1, y2])
    #breakpoint()
    plt.plot([a[0],a[1],a[1],a[0],a[0]],[b[0],b[0],b[1],b[1],b[0]],"-b")
def detected(area):
    group_set(area, (10,10), (100,100))
    group_set(area, (200,100),(202,400))
    return area
def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def neighbour_cells(a,pos,playGround,area,orientation_last):
    cells=[]
    orientation=[]
   # print(orientation_last[0])
    #(-1-1)
    if  pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]-1][pos[1]-1] == 1:
            cells.append([pos[0]-1,pos[1]-1])
            area[pos[0]-1][pos[1]-1] = 2
            if(math.fabs(orientation_last[0]-225)>=180):
                orientation.append([math.fabs(225-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-225)])

    #(0 -1)
    if  pos[0] >= playGround[0] and pos[0] <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]][pos[1]-1] == 1:
            cells.append([pos[0],pos[1]-1]) 
            area[pos[0]][pos[1]-1] = 2
            if(math.fabs(orientation_last[0]-270)>=180):
                orientation.append([math.fabs(270-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-270)])

    #(1 -1)
    if  pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]+1][pos[1]-1] == 1:
            cells.append([pos[0]+1,pos[1]-1])
            area[pos[0]+1][pos[1]-1] = 2
            if(math.fabs(orientation_last[0]-315)>=180):
                orientation.append([math.fabs(315-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-315)])
    #(1 0)
    if  pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        if area[pos[0]+1][pos[1]] == 1:
            cells.append([pos[0]+1,pos[1]])
            area[pos[0]+1][pos[1]] = 2
            if(math.fabs(orientation_last[0]-360)>=180):
                orientation.append([math.fabs(360-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-360)])

    #(1 1)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]+1][pos[1]+1] == 1:
            cells.append([pos[0]+1,pos[1]+1])
            area[pos[0]+1][pos[1]+1] = 2
            if(math.fabs(orientation_last[0]-180)>=180):
                orientation.append([math.fabs(45-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-45)])

    #(0 1)
    if  pos[0] >= playGround[0] and pos[0] <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]][pos[1]+1] == 1:
            cells.append([pos[0],pos[1]+1])
            area[pos[0]][pos[1]+1] = 2
            if(math.fabs(orientation_last[0]-90)>=180):
                orientation.append([math.fabs(90-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-90)])
    
    #(-1 1)
    if  pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]-1][pos[1]+1] == 1:
            cells.append([pos[0]-1,pos[1]+1])
            area[pos[0]-1][pos[1]+1] = 2
            if(math.fabs(orientation_last[0]-135)>=180):
                orientation.append([math.fabs(135-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-135)])

    #(-1 0)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        if area[pos[0]-1][pos[1]]  ==1:
            cells.append([pos[0]-1,pos[1]])
            area[pos[0]-1][pos[1]] = 2
            if(math.fabs(orientation_last[0]-180)>=180):
                orientation.append([math.fabs(180-orientation_last[0])])
            else:
                orientation.append([math.fabs(orientation_last[0]-180)])
    #print(cells)
    return cells,orientation
       
def neighbour_least_cost(cells,pos,goal,orientation,area):
    cost=[]
    least=[0,0,100000,0]
    for i in range(0,len(cells)-1):
        #breakpoint()
        a = distance(cells[i][0],cells[i][1],pos[0],pos[1])+distance(cells[i][0],cells[i][1],goal[0],goal[1])#+orientation[i][0]
        cost.append([cells[i][0],cells[i][1],a])
        if least[2] > cost[i][2]:
            least[0] = cost[i][0]
            least[1] = cost[i][1]
            least[2] = cost[i][2]
            least[3] = orientation[i]
            area[cells[i][0]][cells[i][1]] = 1
            #print(orientation[i])
        #print("Cost:",cost)
        #print("least:",least)
    #plt.plot([pos[0],pos[1]],[least[0],least[1]],"-b")
    #print("final:",least)
    
    return least,area
#def stuckChk():


def main():
    playGround=[0,10000,0,400]
    area = [[1 for _ in range(playGround[3])] for _ in range(playGround[1])]
    #print(area)
    """
    0: new
    1: open
    -1: obstacle
    2: closed
    """
    plt.grid()
    start = [1,1]
    a=[100000,1000000,1000000,100000]
    orientation_last = [0]
    waypoint = [[350,350]]
    plt.axis([0,1000,0,400])
    for i in range (len(waypoint)):
        goal = waypoint[i]
        print(i)
        pos = start
        while pos != goal:
            area = detected(area)
            plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])
            ab, orientation = neighbour_cells(a,pos,playGround,area,orientation_last)
            a,area = neighbour_least_cost(ab,pos,goal,orientation,area)
            plt.pause(0.0001)
            plt.plot(goal[0], goal[1], "-xr")
           # plt.plot(pos[0],pos[1],"-xg")
            plt.plot([0,10000,10000,0,0],[0,0,400,400,0],"-r")
            plt.plot([pos[0],a[0]],[pos[1],a[1]])
            pos[0]=a[0]
            pos[1]=a[1] 
            orientation_last[0]=a[2]
           # print("next step:",a)
            print(pos[0]," ,",a[1])
        print("ALERT: Reached Waypoint",i)
        plt.grid()
    plt.show()
        



if __name__=='__main__':
    main()
