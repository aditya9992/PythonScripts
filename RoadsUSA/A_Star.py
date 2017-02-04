import sys
import heapq
import math
import re
import os
import operator

# For clarity of concepts referenced Wikipedia, CSharpCorner, and Notes provided in the class
# Being a new Learner in Python, coding concepts have been learnt from various online Python tutorial.

# Variables to be used in the program

#search_type = str(sys.argv[1])

#source = str(sys.argv[2])

#dest = str(sys.argv[1])

# defining two lists to save paths and Latitude n Longitude values
LatLong = [[0 for x in range(3)] for y in range(112)]

paths =  [[0 for x in range(3)] for y in range(244)]

# Function to compare the heuristic values of 2 elements
def cmp(val1, val2):
    if val1 < val2:
        return val1
    else:
        return val2

# function to read the data out of the files
def file_read(filename1, filename2):
        file_object = open(filename1, 'r')
        file_object1 = open(filename2, 'r')
        i = 0

        for line in file_object:
            m = [str(s) for s in line.split()]
            LatLong[i][0] = m[0]
            LatLong[i][1] = m[1]
            LatLong[i][2] = m[2]
            i += 1

        j = 0
        for line in file_object1:
            k = [str(s) for s in line.split()]
            paths[j][0], paths[j][1], paths[j][2] = k[0], k[1], k[2]
            paths[j + 1][0], paths[j + 1][1], paths[j + 1][2] = k[1], k[0], k[2]
            j += 2
        return LatLong, paths

# Class for Priority Queue
class PriorityQ:
        def __init__(self):
            self.elements = []

        def isEmpty(self):
            if len(self.elements) == 0:
                return True
            else:
                return False

        def empty(self):
            return len(self.elements) == 0

        def push(self, place1, priority):
            heapq.heappush(self.elements, (priority, place1))

        def pop(self):
            return heapq.heappop(self.elements)[1]

# Class for Node
class Node:
            def __init__(self, node):
                self.id = node
                self.adjacent = {}

            def __str__(self):
                return str([x.id for x in self.adjacent])

            def add_neighbor(self, neighbor, weight=0):
                self.adjacent[neighbor] = weight

            def get_AdjacentKeys(self):
                return self.adjacent.keys()

            def get_id(self):
                return self.id

            def get_weight(self, neighbor):
                return self.adjacent[neighbor]

# Graph Class
class Graph:
            def __init__(self):
                self.vert_dict = {}
                self.num_vertices = 0

            def neighbors(self,id):
                return self.vert_dict[id]

            def add_Edge(self, frm, to, cost=0):
                if frm not in self.vert_dict:
                    self.add_Node(frm)
                if to not in self.vert_dict:
                    self.add_Node(to)

                self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
                self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

            def __iter__(self):
                return iter(self.vert_dict.values())

            def add_Node(self, node):
                self.num_vertices = self.num_vertices + 1
                new_vertex = Node(node)
                self.vert_dict[node] = new_vertex
                return new_vertex

            def get_Node(self, n):
                if n in self.vert_dict:
                    return self.vert_dict[n]
                else:
                    return None

            def get_Nodes(self):
                return self.vert_dict.keys()

            def cost(self, val1, val2, g):
                dis = 0
                for v in g:
                    for w in v.get_AdjacentKeys():
                        vid = v.get_id()
                        wid = w.get_id()
                        if vid == val1:
                            if wid == val2:
                                dis = v.get_weight(w)
                return dis

#initializing the Graph with the values of the distance between the roads

def initialize_Graph():
    g = Graph()
    for i in LatLong:
        g.add_Node(i[0])
    for j in paths:
        g.add_Edge(j[0], j[1], int(j[2]))
    return g

LatLong,paths = file_read(os.getcwd() + '/places.txt', os.getcwd() + '/roads.txt')

g = initialize_Graph()

def fn(g,x):
    min = 1000
    z = ''
    for v in g:
     for w in v.get_AdjacentKeys():
        vid = v.get_id()
        wid = w.get_id()
        if vid == x:
            if min > v.get_weight(w):
                min = v.get_weight(w)
                z = wid
    print('( %s , %s, %3d)'  % ( x, z, min))

def fn1(g,x):
     min = 1000
     z = ''
     for v in g:
      for w in v.get_AdjacentKeys():
         vid = v.get_id()
         wid = w.get_id()
         if vid == x:
             if min > v.get_weight(w):
                 min = v.get_weight(w)
                 z = wid
             print('( %s , %s, %3d)'  % ( vid, z, v.get_weight(w)))

         for v in g:
             print('g.vert_dict[%s]=%s' % (v.get_id(), g.vert_dict[v.get_id()]))



# Heuristic function for A-Star Algorithm

def heuristic(a, b):
    i = 0
    latA, latB, longA, longB = 0.0, 0.0, 0.0 , 0.0

    while i < len(LatLong):
        if a == LatLong[i][0]:
            latA = LatLong[i][1]
            longA = LatLong[i][2]
        if b == LatLong[i][0]:
            latB = LatLong[i][1]
            longB = LatLong[i][2]
        i += 1

    pi = 3.141593

    lat = (float(latA) - float(latB))
    long = math.cos((float(latA) + float(latB)) / 360 * pi) * (float(longA) - float(longB))
    dist = (lat * lat + long * long) ** (1 / 2)

    return dist * 69.5  # Converting into miles

def recon(start, goal, parent):
    current = goal
    path = [current]
    while current != start:
        current = parent[current]
        path.append(current)
    path.reverse() # optional
    return path

# Function to compute A-Star Search Algorithm

def algoRun(algo,gr, start, goal):
    front = PriorityQ()
    front.push(start, 0 + heuristic(goal, start))

    parent_Set = {}
    cost = {}
    parent_Set[start] = None
    cost[start] = 0

    finalpath = []

    while not front.empty():
        current = front.pop()

        if current == goal:
            break
        grph1 = []
        for v in gr:
            if v.get_id() == current:
                findv = re.compile('\w+').findall(str(gr.vert_dict[v.get_id()]))
                for w in findv:
                    vid = v.get_id()
                    wid = w
                    if vid == current:
                        grph1.append(wid)

        finalpath.append(current)
        i = 0

        while i in range(len(grph1)):
            next = grph1[i]
            new_cost = cost[current] + gr.cost(current, next, gr)
            # A-Star Search Algorithm
            if algo == 'astar':
                if next not in cost or new_cost < cost[next]:
                    cost[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    front.push(next, priority)
                    parent_Set[next] = current
                elif next in cost:
                    if new_cost < cost[next]:
                        cost[next] = new_cost
                        priority = new_cost + heuristic(goal, next)
                        front.push(next, priority)
                        parent_Set[next] = current
            # Uniform Search Algorithm
            elif algo == 'uniform':
                    if next not in cost or new_cost < cost[next]:
                        cost[next] = new_cost
                        priority = new_cost
                        front.push(next, priority)
                        parent_Set[next] = current
                    elif next in cost:
                        if new_cost < cost[next]:
                            cost[next] = new_cost
                            priority = new_cost
                            front.push(next, priority)
                            parent_Set[next] = current
            # Greedy Search Algorithm
            elif algo == 'greedy':
                if next not in cost or new_cost < cost[next]:
                    cost[next] = new_cost
                    priority = heuristic(goal, next)
                    front.push(next, priority)
                    parent_Set[next] = current
                elif next in cost:
                    if new_cost < cost[next]:
                        cost[next] = new_cost
                        priority = heuristic(goal, next)
                        front.push(next, priority)
                        parent_Set[next] = current
            i += 1

    cost1 = ''
    if goal in cost:
        cost1 = 'Total Cost to reach: ' + str(cost[goal])
    finalpath.append(goal)

    #x = sorted(cost_so_far.items(), key=operator.itemgetter(1))
    node_exp = 'Number of nodes:' +  str(len(finalpath))

    solpath = recon(start,goal,parent_Set)

    sol_node_num = 'Number of nodes in solution path:' +  str(len(solpath))

    return finalpath, node_exp, solpath, sol_node_num, cost1
