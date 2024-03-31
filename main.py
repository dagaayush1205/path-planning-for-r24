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

        def __init__(self,
                     start,
                     goal,
                     obstacle_list,
                     rand_area,
                     expand_dis=10.0,
                     path_resolution=1,
                     goal_sample_rate=5,
                     max_iter=5000,
                     play_area=[0,100,0,100],
                     robot_dim=[5,5]):
            """
            start:start position[x,y]
            goal: [x,y]
            obstacleList:obstacle position
            randArea: Random Sampling Area[miin,max]
            play_area: boundry
            robot_dim = robot dimensions[X x Y]
            """
            self.start = self.Node(start[0],start[1])
            self.end = self.Node(goal[0],goal[1])
            self.min_rand = rand_area[0]
            self.max_rand = rand_area[1]
            print("start"
            if play_area is not None:
                self.play_area = self.AreaBounds(play_area)
            else:
                self.play_area = None
            self.expand_dis = expand_dis
            self.path_resolution = path_resolution
            self.goal_sample_rate = goal_sample_rate
            self.max_iter = max_iter
            self.obstacle_list = obstacle_list
            self.node_list = []
            self.robot_dim = robot_dim

        def planning(self, animation=True):
            self.node_list = [self.start]
            for i in range(self.amx_iter):
                rnd_node = self.get_random_node()
                nearest_ind = self.get_nearest_node_index(self.node_list,animation = True):
                    rnd_node = self.get_random_node()
                    nearest_ind = self.get_nearest_node_index(self.nodelist, rnd_node)
                    nearest_node = self.node(nearest_node,rnd_node,self.expand_dis)
                    if self.check_if_outside_play_area(new_node,self.play_area) and self.check_collision(new_node,self.obstacle_list,self.robot_dim):
                        self.node_list.append(new_node)
                    if animation and i % 5 == 0:
                        self.draw_graph(rnd_node)
                    if self.calc_dist_to_goal(self.node_list[-1].x,,self.node_list[-1].y) <= self.expand_dis:
                        final_node = self.steer(self.node_list[-1], self.end, self.expand_dis)
                        if self.check_collision(final_node, self.obstacle_list,self.robot_dim):
                            return self.generate_final_course(len(self.node_list) - 1)
                    if animation and i % 5:
                        self.draw_graph(rnd_node)

                return None
            
            def steer(self, from_node, to_node, extend_length=float("inf")):
                
                new_node = self.Node(from_node.x,from_node.y)
                d, theta = self.calc_distance_and_angle(new_node, to_node)

                new_node.path_x = [new_node.x]
                new_node.path_y = [new_node.y]

                if extend_length > d:
                    extend_length = d

                n_expand = math.floor(extend_length / self.path_resolution)

                for _ in range(n_expand):
                    new_node.x += self.path_resolution * math.cos(theta)
                    new_node.y += self.path_resolution * math.sin(theta)
                    new_node.path_x.append(new_node.x)
                    new_node.path_y.append(new_node.y)

                d, _ = self.calc_distance_and_angle(new_node, to_node)
                if d <= self.path_resolution:
                    new_node.path_x.append(to_node.x)
                    new_node.path_y.append(to_node.y)
                    new_node.x = to_node.x
                    new_node.y = to_node.y

                new_node.parent = from_node

                return new_node
            

            def generate_final_course(self, goal_ind):
                path = [[self.end.x,self.end.y]]
                node = self.node_list[goal_ind]
                while node.parent is not None:
                    path.append([node.x,node.y])
                    node = node.parent
                path.append([node.x,node.y])

                return path

            def calc_dist_to_goal(self,x,y):
                dx = x - self.end.x
                dy = y - self.end.y
                return math.hypot(dx,dy)

            def get_random_node(self):
                if random.randint(0, 100) > self.goal_sample_rate:
                    rnd = self.Node(random.uniform(self.min_rand,self.max_rand),random.uniform(self.min_rand,self.max_rand))
                else: 
                    rnd = self.Node(self.end.x, self.end.y)
                return rnd
            def draw_graph(self,rnd=None):
                plt.clf()
                plt.gcf().canvas.mpl_connect('key_release_event',lambda event: [exit(0) if event.key == 'escape' else None])
                plt.plot(
