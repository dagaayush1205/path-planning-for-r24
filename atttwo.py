import math
import matplotlib.pyplot as plt
import numpy as np
from obs import *
def obstacle(area):
    obsatcles = obs.obstacles()
    for i in len(obs):
        if obs[i]
def main():
    area = np.full((100,100,1),0)
    """
    0: new
    1: open
    -1: obstacle
    """
    start = [0,0]
    waypoint = [[90,90],[75,80],[60,70]]
    for i in range (len(waypoint)):
        goal = waypoint[i]
        obstacle(area)
if __name__=='__main__':
    main()
