#code starts here
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas as pd
from csv import writer
fig, ax = plt.subplots()
df = pd.read_csv("point.csv")
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
def map():

    for i in range (0,99):
        for j in range (0,99):
            RRT.grid[i,j,0]=[i+1,j+1,0]

    for i in range (0,99):
        for j in range (0,99):
            print(RRT.grid[i,j,0])
map()
