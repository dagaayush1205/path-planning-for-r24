Introduction and attributes

Also known as the Dstar algorithm, it is a variation of the Astar path planning algorithm.

In this algorithm each cell has some attributes related to it such as cost, parent cell and state.

    Cost - it is the sum of the expense expected by the rover to traverse to a point and the heuristic value of that cell to the goal.
    Parent cell - each cell has a parent cell associated with it. Which points the location of the cell it was moved from
    State -
        NEW - unexplored cell
        OPEN - cells that being considered for expansion
        CLOSED - cells that have been already considered for expansion
        OBSTACLE - cell is an obstacle

Algorithm

Initially, we set our starting point as the open cell,  we then check its neighbouring cell, which are new(in this case as it is our starting iteration),  the neighbouring cells must fulfil some conditions such as; it is not an OBSTACLE, it in the current playground and it that is a NEW cell.  

We change the state neighbour cells to OPEN cell from NEW cell  and calculate the cost, the parent cell here the cell that was previously associated with it. In this case it is the start cell. The cell from whom the neighbours are calculated is made to state CLOSED as it has explored.

We start over, consider all the OPEN cells and explore their neighbours and continue with the above process until we reach the goal.

From here we backward track the parent cell of the goal to achieve an optimum path.

To improve the code, the arena has been divided into grids of cell 20cm x 20cm. And a size of not more than 100. The rover individually traverses through each grid.

We found this process to be better than considering the entire arena at once 
