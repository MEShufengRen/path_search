# Shufeng Ren
# 2019/3/21
# Description: Define main function to implement path search algrithms

from graphSearch import *
from build_world import *
from map_example import *


def main():
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
    scene = input('Please choose one scene from 1~4:\n')
    graph = switch_map[scene]
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
        start, goal = (5, 45), (45, 5)
        ax, ann_iterate, ann_path = plot_init_map_noclick(graph, method, start, goal)
    flag, graph_result, update_ax = switch_search_method[method](graph, start, goal, ax, ann_iterate, animation)
    if flag == 'Successful':
        path, path_length = reconstruct_path(graph_result, start, goal)
        plot_search_result(path, path_length, update_ax, ann_path)


if __name__ == '__main__':
    main()
