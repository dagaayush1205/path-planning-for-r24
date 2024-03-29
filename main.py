#code starts here
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
#working arena size is 10m x 4m
# i have take a precision of 1cm and taking every grid to be 1000 x 400 resolution
class RRT:
    grid = np.full((101,101,1),-1)
    # the grid has other values including obstacle size which will range from 0 to 1
    # it also has orientation of the grid, all of them have -1 by default in case that
    # it remains unexplored, in simple terms, rover has give -1 to all unexplored part
    # since everything that it must include must be in whole numbers
    # format(x,y,z,orientation wrt to rover, cost)
    #note for testing stage the area is 100x100units only
    class node:

        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.path_x = []
            self.path_y = []
            self.parent = None

        class AreaBounds:
            def __init__(self,area):
                self.xmin = float(area[0])
                self.xmax = float(area[1])
                self.ymin = float(area[2])
                self.ymax = float(area[3])
                #area([xmin,xmax,ymin,ymax])

        def __init__(self,start,goal)
