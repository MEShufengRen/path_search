# Shufeng Ren
# 2019/3/21
# Description: Define 8 functions to build the robot world and show the animation

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


def extract_visited_ponits(graph):
    visited_x = []
    visited_y = []
    for node_list in graph.Nodes:
        for node in node_list:
            if node.visited:
                visited_x.append(node.xpos)
                visited_y.append(node.ypos)
    visited_list = [visited_x,visited_y]
    return visited_list


def create_rec(verts):
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='orange', lw=0.5)
    return patch


def plot_init_map(graph, method):
    plt.ion()  # open interactive model
    figure = plt.figure(1)
    ax = figure.add_subplot(111)
    # set width and height of scene
    ax.set_xlim(-0.15*graph.width, 1.15*graph.width)
    ax.set_ylim(0, 1.5*graph.height)
    ax.plot([0,0,graph.width,graph.width],[0,graph.height,graph.height,0],
            'k-', lw=2, label="Map Range", zorder=3)
    plt.legend(loc='upper right')
    # set no ticks
    plt.xticks([], [])
    plt.yticks([], [])
    # plot the obsctacles
    for obc in graph.walls:
        vert = [
           (obc[0], obc[1]),  # left, bottom
           (obc[0], obc[1]+obc[3]),  # left, top
           (obc[0]+obc[2], obc[1]+obc[3]),  # right, top
           (obc[0]+obc[2], obc[1]),  # right, bottom
           (obc[0], obc[1]),  # ignored
        ]
        patch = create_rec(vert)
        ax.add_patch(patch)
    start, goal = mouse_click_position()
    # plot start point and goal point
    ax.plot(start[0], start[1], 'bs', markersize=5, label='start point', zorder=3)
    ax.plot(goal[0], goal[1], 'gs', markersize=5, label='goal point',zorder=3)
    ax.plot([],[], marker='s',c='0.5',markersize=1, zorder=1,
            linestyle='', alpha=0.8, fillstyle='top', label='visited points')
    plt.legend()
    # set title infomation
    annotation_initial = method+' progress\n'+'start: (%.1f,%.1f) | goal: (%.1f,%.1f)\n' \
                         %(start[0],start[1],goal[0],goal[1])
    annotation_iteration = 'Iteration/Visited: 0 | Queue size: 0\n'
    annotation_path = 'Path length: 0.0'

    plt.annotate(annotation_initial, xy=(0.05,0.80), xycoords='axes fraction', fontsize=10)
    ann_iterate = plt.annotate(annotation_iteration, xy=(0.05,0.74), xycoords='axes fraction', fontsize=10)
    ann_path = plt.annotate(annotation_path, xy=(0.05,0.72), xycoords='axes fraction', fontsize=10)

    return start, goal, ax, ann_iterate, ann_path


def plot_init_map_noclick(graph, method, start, goal):
    plt.ion()  # open interactive model
    figure = plt.figure(1)
    ax = figure.add_subplot(111)
    # set width and height of scene
    ax.set_xlim(-0.15*graph.width, 1.15*graph.width)
    ax.set_ylim(0, 1.5*graph.height)
    ax.plot([0,0,graph.width,graph.width],[0,graph.height,graph.height,0],
            'k-', lw=2, label="Map Range", zorder=3)
    plt.legend(loc='upper right')
    # set no ticks
    plt.xticks([], [])
    plt.yticks([], [])
    # plot the obsctacles
    for obc in graph.walls:
        vert = [
           (obc[0], obc[1]),  # left, bottom
           (obc[0], obc[1]+obc[3]),  # left, top
           (obc[0]+obc[2], obc[1]+obc[3]),  # right, top
           (obc[0]+obc[2], obc[1]),  # right, bottom
           (obc[0], obc[1]),  # ignored
        ]
        patch = create_rec(vert)
        ax.add_patch(patch)
    # plot start point and goal point
    ax.plot(start[0], start[1], 'bs', markersize=5, label='start point', zorder=3)
    ax.plot(goal[0], goal[1], 'gs', markersize=5, label='goal point',zorder=3)
    ax.plot([],[], marker='s',c='0.5',markersize=1, zorder=1,
            linestyle='', alpha=0.8, fillstyle='top', label='visited points')
    plt.legend()
    # set title infomation
    annotation_initial = method+' progress\n'+'start: (%.1f,%.1f) | goal: (%.1f,%.1f)\n' \
                         %(start[0],start[1],goal[0],goal[1])
    annotation_iteration = 'Iteration/Visited: 0 | Queue size: 0\n'
    annotation_path = 'Path length: 0.0'

    plt.annotate(annotation_initial, xy=(0.05,0.80), xycoords='axes fraction', fontsize=10)
    ann_iterate = plt.annotate(annotation_iteration, xy=(0.05,0.74), xycoords='axes fraction', fontsize=10)
    ann_path = plt.annotate(annotation_path, xy=(0.05,0.72), xycoords='axes fraction', fontsize=10)

    return ax, ann_iterate, ann_path


def plot_visited_point(graph, num_iterate, queue_size, ax, ann_iterate):
    plt.ion()  # open interactive model
    # plot visited points
    visited = extract_visited_ponits(graph)
    ax.plot(visited[0],visited[1], marker='s',c='0.5',markersize=1, zorder=1,
            linestyle='', alpha=0.8, fillstyle='top')
    # update title infomation
    annotation_string = 'Iteration/Visited: %d | Queue size: %d\n' %(num_iterate, queue_size)
    ann_iterate.set_text(annotation_string)
    plt.pause(0.00000001)
    return ax


def plot_search_result(path, path_length, ax, ann_path):
    plt.ion()  # open interactive model
    # plot path
    ax.plot(path[0], path[1], 'r-', lw=2, label='path',zorder=2)
    # show legend
    plt.legend()
    # update title infomation
    annotation_string = 'Path length: %.1f' %(path_length)
    ann_path.set_text(annotation_string)
    # plt.pause(3)
    plt.ioff()
    plt.show()

def mouse_click_position():
    pos = plt.ginput(2)
    start = pos[0]
    goal = pos[1]
    start = (int(start[0]), int(start[1]))
    goal = (int(goal[0]), int(goal[1]))
    return start, goal


def reconstruct_path(graph, start, goal):
    current = graph.Nodes[goal[0]][goal[1]]
    path_x = []
    path_y = []
    while current.pos != start:
        path_x.append(current.xpos)
        path_y.append(current.ypos)
        current = current.parent
    path_x.append(start[0])
    path_y.append(start[1])
    path=[path_x,path_y]
    path_length = graph.Nodes[goal[0]][goal[1]].distance
    return path, path_length
