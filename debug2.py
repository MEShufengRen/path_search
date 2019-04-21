from graphSearch import *
from build_world import *


#  Define the map
##############################Scene 1####################################
# graph = Map(100, 100)
# graph.walls = [[20, 5, 10, 90], [50, 0, 30, 70], [50, 80, 40, 20]]
##############################Scene 2####################################
graph = Map(50, 50)
graph.walls = [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]]
# animation = True
# click = True
# method = 'A-star'
switch_search_method = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}



def main():
    scene = input('Please choose one scene from 1~3:\n')
    method = input('Please choose one path search method from following:\n'
                   'A-star  ' 'Dijkstra  ' 'DFS  ' 'BFS  ' 'Greedy\n'
                   'press \'q\' to quit progress\n')
    if method is 'q':
        return
    elif method not in switch_search_method:
        print('Check the word spell\n')
        method = input('Please choose one path search method from following:\n'
                   'A-star  ' 'Dijkstra  ' 'DFS  ' 'BFS  ' 'Greedy\n'
                   'press \'q\' to quit progress\n')
    animation = input('If open animation? y/n\n')
    if animation == 'y':
        animation = True
    else:
        animation = False

    click = input('If select start and goal position by hand? y/n\n')
    if click == 'y':
        print('Please choose start and goal position on the map! Showing \'x corss\' means choose successfully\n')
        start, goal, ax, ann_iterate, ann_path = plot_init_map(graph, method)
    else:
        start, goal = (2, 2), (45, 30)
        ax, ann_iterate, ann_path = plot_init_map_noclick(graph, method, start, goal)

    flag, graph_result, update_ax = switch_search_method[method](graph, start, goal, ax, ann_iterate, animation)
    if flag == 'Successful':
        path, path_length = reconstruct_path(graph_result, start, goal)
        plot_search_result(path, path_length, update_ax, ann_path)
        plt.ion()


if __name__ == '__main__':
    main()
