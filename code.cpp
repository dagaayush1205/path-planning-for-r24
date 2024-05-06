#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
class PathPlanning
{
public:	
	void obs_plot(int x1, int x2, int y1, int y2);
	float distance(int x1, int x2, int y1, int y2);
	float cost_from_start(int curr_pos, int curr_posy, int next_posx, int next_posy);
	float heuristic_cost(int curr_posx,int curr_posy, int goal[]);
	float final_cost(int curr_posx, int curr_posy, int next_posx, int next_posy, int goal[]);
	int grid_size[4];
	PathPlanning(){
		cout << "Enter Grid size" << endl;
		cin>>grid_size[0]>>grid_size[1]>>grid_size[2]>>grid_size[3]; 
		vector<vector<int>> area_state(grid_size[1], vector<int>(grid_size[3], 0));
                vector<vector<float>> area_cost(grid_size[1], vector<float>(grid_size[3], 0));
                vector<vector<int>> area_parentx(grid_size[1], vector<int>(grid_size[3], 0));
                vector<vector<int>> area_parenty(grid_size[1], vector<int>(grid_size[3], 0));
	}	

};


PathPlanning::distance(int x1, int x2, int y1, int y2){
	return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2);
}


PathPlanning::float cost_from_start(int curr_pos, int curr_posy, int next_posx, int next_posy){
	return area_cost[curr_posx][curr_posy] + distance(curr_posx,curr_posy,next_posx,next_posy)
}


PathPlanning::float heuristic_cost(int curr_posx,int curr_posy, int goal[]){
	 return distance(curr_posx,curr_posy,goal[0],goal[1])
	 }


PathPlanning::float final_cost(int curr_posx, int curr_posy, int next_posx, int next_posy){
	return float cost_from_start(int curr_posx, int curr_posy, int next_posx, int next_posy) + heuristic_cost(int curr_posx, int curr_posy)
}


PathPlanning::std::vector<std::vector<int>> neighbour_cells(int pos[]):
    vector<vector<int>> cells(, vector<int>(2, 0));
	#(-1-1)
    if  pos[0]-1 >= grid_size[0] and pos[0]-1 <= grid_size[1] and pos[1]-1 >= grid_size[2] and pos[1]-1 <= grid_size[3] and area_state[pos[0]-1][pos[1]-1] == 0:

        cells.append([pos[0]-1,pos[1]-1])
        area_parentx[pos[0]-1][pos[1]-1] = pos[0]
        area_parenty[pos[0]-1][pos[1]-1] = pos[1]
        area_state[pos[0]-1][pos[1]-1] = 1
        area_cost[pos[0]-1][pos[1]-1] = final_cost(pos[0],pos[1],pos[0]-1,pos[1]-1,goal,area_cost)

    #(0 -1)
    if  pos[0] >= grid_size[0] and pos[0] <= grid_size[1] and pos[1]-1 >= grid_size[2] and pos[1]-1 <= grid_size[3]:
        if area_state[pos[0]][pos[1]-1] == 0:
            cells.append([pos[0],pos[1]-1])
            area_parentx[pos[0]][pos[1]-1] = pos[0]
            area_parenty[pos[0]][pos[1]-1] = pos[1]
            area_state[pos[0]][pos[1]-1] = 1
            area_cost[pos[0]][pos[1]-1] = final_cost(pos[0],pos[1],pos[0],pos[1]-1)

    #(+1 -1)
    if  pos[0]+1 >= grid_size[0] and pos[0]+1 <= grid_size[1] and pos[1]-1 >= grid_size[2] and pos[1]-1 <= grid_size[3]:
        if area_state[pos[0]+1][pos[1]-1] == 0:
            cells.append([pos[0]+1,pos[1]-1])
            area_parentx[pos[0]+1][pos[1]-1] = pos[0]
            area_parenty[pos[0]+1][pos[1]-1] = pos[1]
            area_state[pos[0]+1][pos[1]-1] = 1
            area_cost[pos[0]+1][pos[1]-1] = final_cost(pos[0],pos[1],pos[0]+1,pos[1]-1,)

    #(+1 0)
    if  pos[0]+1 >= grid_size[0] and pos[0]+1 <= grid_size[1] and pos[1] >= grid_size[2] and pos[1] <= grid_size[3]:
        if area_state[pos[0]+1][pos[1]] == 0:
            cells.append([pos[0]+1,pos[1]])
            area_parentx[pos[0]+1][pos[1]] = pos[0]
            area_parenty[pos[0]+1][pos[1]] = pos[1]
            area_state[pos[0]+1][pos[1]] = 1
            area_cost[pos[0]+1][pos[1]] = final_cost(pos[0],pos[1],pos[0]+1,pos[1])

    #(+1 +1)
    if pos[0]+1 >= grid_size[0] and pos[0]+1 <= grid_size[1] and pos[1]+1 >= grid_size[2] and pos[1]+1 <= grid_size[3]:
        if area_state[pos[0]+1][pos[1]+1] == 0:
            cells.append([pos[0]+1,pos[1]+1])
            area_parentx[pos[0]+1][pos[1]+1] = pos[0]
            area_parenty[pos[0]+1][pos[1]+1] = pos[1]
            area_state[pos[0]+1][pos[1]+1][3] = 1
            area_cost[pos[0]+1][pos[1]+1][2] = final_cost(pos[0],pos[1],pos[0]+1,pos[1]+1)

    #(0 +1)
    if  pos[0] >= grid_size[0] and pos[0] <= grid_size[1] and pos[1]+1 >= grid_size[2] and pos[1]+1 <= grid_size[3]:
        if area_state[pos[0]][pos[1]+1][3] == 0:
            cells.append([pos[0],pos[1]+1])
            area_parentx[pos[0]][pos[1]+1] = pos[0]
            area_parenty[pos[0]][pos[1]+1] = pos[1]
            area_state[pos[0]][pos[1]+1] = 1
            area_cost[pos[0]][pos[1]+1] = final_cost(pos[0],pos[1],pos[0],pos[1]+1)
 #(-1 +1)
    if  pos[0]-1 >= grid_size[0] and pos[0]-1 <= grid_size[1] and pos[1]+1 >= grid_size[2] and pos[1]+1 <= grid_size[3]:
        if area_state[pos[0]-1][pos[1]+1] == 0:
            cells.append([pos[0]-1,pos[1]+1])
            area_parentx[pos[0]-1][pos[1]+1] = pos[0]
            area_parenty[pos[0]-1][pos[1]+1]= pos[1]
            area_state[pos[0]-1][pos[1]+1] = 1
            area_cost[pos[0]-1][pos[1]+1] = final_cost(pos[0],pos[1],pos[0]-1,pos[1]+1)

    #(-1 0)
    if pos[0]-1 >= grid_size[0] and pos[0]-1 <= grid_size[1] and pos[1] >= grid_size[2] and pos[1] <= grid_size[3]:
        if area_state[pos[0]-1][pos[1]]  == 0:
            cells.append([pos[0]-1,pos[1]])
            area_parentx[pos[0]-1][pos[1]] = pos[0]
            area_parenty[pos[0]-1][pos[1]] = pos[1]
            area_state[pos[0]-1][pos[1]] = 1
            area_cost[pos[0]-1][pos[1]] = final_cost(pos[0],pos[1],pos[0]-1,pos[1])

    area_state[pos[0]][pos[1]] = 2 # closed the current cell
    pos = least_cost(check_open_cells())
    return pos

int main(){
    main_function();
    return 0;
}
