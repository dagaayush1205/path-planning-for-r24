import math
from sys import maxsize
import matplotlib.pyplot as plt

show animation = True

class State:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.parent = None
        self.state = "."
        self.t = "new"
        self.h = 0
        self.k = 0

        def cost(self,state):
            if self.state == "#" or state.state == "#":
                return maxsize
            return math.sqrt(math.pow((self.x-state.x),2)+
                             math.pow((self.y - state.y),2))

        def set_state(self,state):
           if state not in ["s",".","#","e","*"]:
               return
           self.state = state

class Map:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.map = self.init_map()

    def init_map(self):
        map_list = []
        for i in range(self.col):
            tmp = []
            for j in range (self.col):
                tmp.append(State(i,j))
                map_list.append(tmp)
            return map_list

    def get_neighors(self, state):
        state_list = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    continue
                if state.x + i<0 or state.x +i >= self.row:
                    continue
                if state.y + j < 0 or state.y + j >= self.col:
                    continue
                state_list append(self.map[state.x + i][[state.y +j])
        return state_list

    def set_obstacle(self, point_list):
        for x,y in point_list
