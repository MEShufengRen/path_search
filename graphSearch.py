# Shufeng Ren, Jiarui Li
# 2019/3/21
# Description: Define five path search functions and a dictionary: switch_search_method

from pathsearch_class import *
from build_world import plot_visited_point
import math


def euclidean_distance(current,goal):
    return math.sqrt(math.pow(current[0]-goal[0],2)+math.pow(current[1]-goal[1],2))


def dijkstra_search(graph, start, goal, ax, ann_iterate, animation):
    search_iterate = True
    num_iterate = 0
    graph.Nodes[start[0]][start[1]].distance = 0
    visited_queue = PriorityQueue()
    visited_queue.put(start, 0)

    while not visited_queue.empty():
        num_iterate = num_iterate+1
        current = visited_queue.get()
        graph.Nodes[current[0]][current[1]].visited = True
        graph.Nodes[current[0]][current[1]].queued = False
        if current == goal:
            search_iterate = False
            break
        for nb in graph.neighbors(current):
            if not graph.Nodes[nb[0]][nb[1]].visited:
                if not graph.Nodes[nb[0]][nb[1]].queued:
                    graph.Nodes[nb[0]][nb[1]].queued = True
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].distance)
                elif graph.Nodes[nb[0]][nb[1]].distance > graph.Nodes[current[0]][current[1]].distance + 1:
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].distance)
        if animation:
            plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    if not search_iterate:
        flag = 'Successful'
        ax = plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    else:
        flag = 'Failed'
    return flag, graph, ax


def astar_search(graph, start, goal, ax, ann_iterate, animation):
    search_iterate = True
    num_iterate = 0
    graph.Nodes[start[0]][start[1]].distance = 0
    visited_queue = PriorityQueue()
    visited_queue.put(start, 0)

    while not visited_queue.empty():
        num_iterate = num_iterate+1
        current = visited_queue.get()
        graph.Nodes[current[0]][current[1]].visited = True
        graph.Nodes[current[0]][current[1]].queued = False
        if current == goal:
            search_iterate = False
            break
        for nb in graph.neighbors(current):
            if not graph.Nodes[nb[0]][nb[1]].visited:
                if not graph.Nodes[nb[0]][nb[1]].queued:
                    graph.Nodes[nb[0]][nb[1]].queued = True
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].priority = euclidean_distance(nb,goal) + graph.Nodes[nb[0]][nb[1]].distance
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].priority)
                elif graph.Nodes[nb[0]][nb[1]].distance > graph.Nodes[current[0]][current[1]].distance + 1:
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].priority = euclidean_distance(nb,goal) + graph.Nodes[nb[0]][nb[1]].distance
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].priority)
        if animation:
            plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    if not search_iterate:
        flag = 'Successful'
        ax = plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    else:
        flag = 'Failed'
    return flag, graph, ax


def greedy_search(graph, start, goal, ax, ann_iterate, animation):
    search_iterate = True
    num_iterate = 0
    graph.Nodes[start[0]][start[1]].distance = 0
    visited_queue = PriorityQueue()
    visited_queue.put(start, 0)

    while not visited_queue.empty():
        num_iterate = num_iterate+1
        current = visited_queue.get()
        graph.Nodes[current[0]][current[1]].visited = True
        graph.Nodes[current[0]][current[1]].queued = False
        if current == goal:
            search_iterate = False
            break
        for nb in graph.neighbors(current):
            if not graph.Nodes[nb[0]][nb[1]].visited:
                if not graph.Nodes[nb[0]][nb[1]].queued:
                    graph.Nodes[nb[0]][nb[1]].queued = True
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].priority = euclidean_distance(nb,goal)
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].priority)
                elif graph.Nodes[nb[0]][nb[1]].distance > graph.Nodes[current[0]][current[1]].distance + 1:
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].priority = euclidean_distance(nb,goal)
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].priority)
        if animation:
            plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    if not search_iterate:
        flag = 'Successful'
        ax = plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    else:
        flag = 'Failed'
    return flag, graph, ax


def dfs_search(graph, start, goal, ax, ann_iterate, animation):
    search_iterate = True
    num_iterate = 0
    graph.Nodes[start[0]][start[1]].distance = 0
    visited_queue = list()
    visited_queue.append(start)

    while len(visited_queue)>0:
        num_iterate = num_iterate+1
        current = visited_queue.pop()
        graph.Nodes[current[0]][current[1]].visited = True
        graph.Nodes[current[0]][current[1]].queued = False
        if current == goal:
            search_iterate = False
            break
        for nb in graph.neighbors(current):
            if not graph.Nodes[nb[0]][nb[1]].visited and not graph.Nodes[nb[0]][nb[1]].queued:
                graph.Nodes[nb[0]][nb[1]].queued = True
                graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                visited_queue.append(nb)
            if graph.Nodes[nb[0]][nb[1]].distance > graph.Nodes[current[0]][current[1]].distance + 1:
                graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
        if animation:
            plot_visited_point(graph, num_iterate, len(visited_queue), ax, ann_iterate)
    if not search_iterate:
        flag = 'Successful'
        ax = plot_visited_point(graph, num_iterate, len(visited_queue), ax, ann_iterate)
    else:
        flag = 'Failed'
    return flag, graph, ax


def bfs_search(graph, start, goal, ax, ann_iterate, animation):
    search_iterate = True
    num_iterate = 0
    graph.Nodes[start[0]][start[1]].distance = 0
    visited_queue = Queue()
    visited_queue.put(start)

    while not visited_queue.empty():
        num_iterate = num_iterate+1
        current = visited_queue.get()
        graph.Nodes[current[0]][current[1]].visited = True
        graph.Nodes[current[0]][current[1]].queued = False
        if current == goal:
            search_iterate = False
            break
        for nb in graph.neighbors(current):
            if not graph.Nodes[nb[0]][nb[1]].visited:
                if not graph.Nodes[nb[0]][nb[1]].queued:
                    graph.Nodes[nb[0]][nb[1]].queued = True
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb)
                elif graph.Nodes[nb[0]][nb[1]].distance > graph.Nodes[current[0]][current[1]].distance + 1:
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
        if animation:
            plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    if not search_iterate:
        flag = 'Successful'
        ax = plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    else:
        flag = 'Failed'
    return flag, graph, ax


switch_search_method = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
