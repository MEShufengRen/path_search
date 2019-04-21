# Shufeng Ren, Jiarui Li
# 2019/3/21
# Description: Define four class: Queue, PriorityQueue, Node, Map

import collections
import heapq


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

    def len(self):
        return len(self.elements)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def len(self):
        return len(self.elements)

class Node:
    def __init__(self,position):
        self.pos = position
        self.xpos = position[0]
        self.ypos = position[1]
        self.parent = None
        self.visited = False
        self.queued = False
        self.distance = 10000
        self.priority = None


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.Nodes = self.init_graph_node()

    def bounds_detect(self,result):
        return 0 <= result[0] <= self.width and 0 <= result[1] <= self.height

    def collision_detect(self,result):
        for wall in self.walls:
            if wall[0]-1<result[0]<wall[0]+wall[2]+1 and wall[1]-1<result[1]<wall[1]+wall[3]+1:
                return False
        return True

    def neighbors(self, node):
        (x, y) = node
        results = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        results = filter(self.bounds_detect, results)
        results = filter(self.collision_detect, results)
        return results

    def init_graph_node(self):
        g = [[Node((j,i))for i in range(self.width+1)]for j in range(self.height+1)]
        return g


