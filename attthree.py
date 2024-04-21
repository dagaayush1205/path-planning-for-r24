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
    #group_set(area, (10,10), (100,100))
    #group_set(area, (200,100),(202,400))


def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))


def cost_from_start(curr_posx,curr_posy,next_pos,area):
    return area[curr_posx][curr_posy][1] + distance(curr_posx,curr_posy,next_pos[0],next_pos[1])


def heuristic_cost(curr_posx,curr_posy,goal):
    return distance(curr_posx,curr_posy,goal[0],goal[1])


def final_cost(curr_posx,curr_posy,next_pos,goal,area):
    return cost_from_start(curr_posx,curr_posy,next_pos,area) + heuristic_cost(curr_posx,curr_posy,goal)


def neighbour_cells(pos,playGround,area,goal):
    cells=[]
    #(-1-1)
    if  pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]-1][pos[1]-1][3] == 0:
            cells.append([pos[0]-1,pos[1]-1])
            area[pos[0]-1][pos[1]-1][0] = pos[0]
            area[pos[0]-1][pos[1]-1][1] = pos[1]
            area[pos[0]-1][pos[1]-1][3] = 1
            area[pos[0]-1][pos[1]-1][2] = final_cost(pos[0],pos[1],pos[0]-1,pos[1]-1,goal,area)

    #(0 -1)
    if  pos[0] >= playGround[0] and pos[0] <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]][pos[1]-1][3] == 0:
            cells.append([pos[0],pos[1]-1]) 
            area[pos[0]][pos[1]-1][0] = pos[0]
            area[pos[0]][pos[1]-1][1] = pos[1]
            area[pos[0]][pos[1]-1][3] = 1
            area[pos[0]][pos[1]-1][2] = final_cost(pos[0],pos[1],pos[0],pos[1]-1,goal,area)

    #(+1 -1)
    if  pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1]-1 >= playGround[2] and pos[1]-1 <= playGround[3]:
        if area[pos[0]+1][pos[1]-1][3] == 0:
            cells.append([pos[0]+1,pos[1]-1])
            area[pos[0]+1][pos[1]-1][0] = pos[0]
            area[pos[0]+1][pos[1]-1][1] = pos[1]
            area[pos[0]+1][pos[1]-1][3] = 1
            area[pos[0]+1][pos[1]-1][2] = final_cost(pos[0],pos[1],pos[0]+1,pos[1]-1,goal,area)

    #(+1 0)
    if  pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        if area[pos[0]+1][pos[1]][3] == 0:
            cells.append([pos[0]+1,pos[1]])
            area[pos[0]+1][pos[1]][0] = pos[0]
            area[pos[0]+1][pos[1]][1] = pos[1]
            area[pos[0]+1][pos[1]][3] = 1
            area[pos[0]+1][pos[1]][2] = final_cost(pos[0],pos[1],pos[0]+1,pos[1],goal,area)

    #(+1 +1)
    if pos[0]+1 >= playGround[0] and pos[0]+1 <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]+1][pos[1]+1][3] == 0:
            cells.append([pos[0]+1,pos[1]+1])
            area[pos[0]+1][pos[1]+1][0] = pos[0]
            area[pos[0]+1][pos[1]+1][1] = pos[1]
            area[pos[0]+1][pos[1]+1][3] = 1
            area[pos[0]+][pos[1]+1][2] = final_cost(pos[0],pos[1],pos[0]+1,pos[1]+1,goal,area)

    #(0 +1)
    if  pos[0] >= playGround[0] and pos[0] <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]][pos[1]+1][3] == 0:
            cells.append([pos[0],pos[1]+1])
            area[pos[0]][pos[1]+1][0] = pos[0]
            area[pos[0]][pos[1]+1][1] = pos[1]
            area[pos[0]][pos[1]+1][3] = 1
            area[pos[0]][pos[1]+1][2] = final_cost(pos[0],pos[1],pos[0],pos[1]+1,goal,area)
    
    #(-1 +1)
    if  pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1]+1 >= playGround[2] and pos[1]+1 <= playGround[3]:
        if area[pos[0]-1][pos[1]+1][3] == 0:
            cells.append([pos[0]-1,pos[1]+1])
            area[pos[0]-1][pos[1]+1][0] = pos[0]
            area[pos[0]-1][pos[1]+1][1] = pos[1]
            area[pos[0]-1][pos[1]+1][3] = 1
            area[pos[0]-1][pos[1]+1][2] = final_cost(pos[0],pos[1],pos[0]-1,pos[1]+1,goal,area)

    #(-1 0)
    if pos[0]-1 >= playGround[0] and pos[0]-1 <= playGround[1] and pos[1] >= playGround[2] and pos[1] <= playGround[3]:
        if area[pos[0]-1][pos[1]][3]  == 0:
            cells.append([pos[0]-1,pos[1]])
            area[pos[0]-1][pos[1]][0] = pos[0]
            area[pos[0]-1][pos[1]][1] = pos[1]
            area[pos[0]-1][pos[1]][3] = 1
            area[pos[0]-1][pos[1]][2] = final_cost(pos[0],pos[1],pos[0]-1,pos[1],goal,area)

    area[pos[0]][pos[1]][3] = 2 # closed the current cell
    return cells


def neighbour_least_cost(cells,pos,goal,orientation,area):
    cost=[]
    least=[0,0,100000,0]
    for i in range(0,len(cells)-1):
        a = distance(cells[i][0],cells[i][1],pos[0],pos[1])+distance(cells[i][0],cells[i][1],goal[0],goal[1])#+orientation[i][0]
        if area[cells[i][0]][cells[i][1]] == 2:
            a+=1000
            area[cells[i][0]][cells[i][1]] = 1
            print(cells[i][0]," ",cells[i][1])
        cost.append([cells[i][0],cells[i][1],a])
        
        if least[2] > cost[i][2]:
            least[0] = cost[i][0]
            least[1] = cost[i][1]
            least[2] = cost[i][2]
            #least[3] = orientation[i]

            #print(orientation[i])
    print("Cost:",cost)
        #print("least:",least)
    #plt.plot([pos[0],pos[1]],[least[0],least[1]],"-b")
    #print("final:",least)
    return least,area


def least_cost():

def main():
    playGround=[0,100,0,100]

    """
    0: new
    1: open
    -1: obstacle
    2: closed
    3: blocked
    """

    plt.grid()
    start=[0,0]
    waypoint=[[70,70]]
    area = [[[1 for _ in range(playGround[3])] for _ in range(playGround[1])] for _ in range(4)]
    for i in range (len(waypoint)):
        goal = waypoint[i]
        print(i)
        pos = start
        while pos != goal:
            area = detected(area)
            plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])
            ab, orientation, cells_last = neighbour_cells(pos,playGround,area,goal)
            a,area = neighbour_least_cost(ab,pos,goal,orientation,area)
            plt.pause(0.01)
            plt.plot(goal[0], goal[1], "-xr")
           # plt.plot(pos[0],pos[1],"-xg")
            plt.plot([0,10000,10000,0,0],[0,0,400,400,0],"-r")
            plt.plot([pos[0],a[0]],[pos[1],a[1]],"-g")
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