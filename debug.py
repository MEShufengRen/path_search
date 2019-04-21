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


def plot_search_result(ax, graph, start, goal, path, path_length, method, num_iterate):
    # plot visited points
    visited = extract_visited_ponits(graph)
    ax.plot(visited[0],visited[1], marker='s',c='0.8',markersize=3,
            linestyle='', alpha=0.8, fillstyle='none', label='visited points')
    # plot start point and goal point
    ax.plot(start[0], start[1], 'bs', markersize=5, label='start point')
    ax.plot(goal[0], goal[1], 'gs', markersize=5, label='goal point')
    # plot path
    ax.plot(path[0], path[1], 'r-', lw=2, label='path')
    # show legend
    ax.legend()
    # show title infomation
    annotation_string = method+' progress\n'
    annotation_string += 'Iteration/Visited: %d \n'%(num_iterate)
    annotation_string += 'start: (%.1f,%.1f) | goal: (%.1f,%.1f)\n' \
                         %(start[0],start[1],goal[0],goal[1])
    annotation_string += 'path length: %.1f' %(path_length)
    plt.annotate(annotation_string, xy=(0.05,0.75), xycoords='axes fraction',
                 backgroundcolor='b', fontsize=12,bbox=dict(facecolor='blue', alpha=0.5))
    plt.show()


def plot_init_map(graph):
    fig, ax = plt.subplots()
    # set width and height of scene
    ax.set_xlim(-10, graph.width+10)
    ax.set_ylim(0, graph.height+40)
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
    plt.show()
    return fig, ax


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

