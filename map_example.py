# Shufeng Ren
# 2019/3/21
# Description: User could design maps here (Four default maps exist)

from pathsearch_class import Map
#  Define the map

# graph = Map(100, 100)
# graph.walls = [[20, 5, 10, 90], [50, 0, 30, 70], [50, 80, 40, 20]]
##############################Scene 1: Empty####################################
scene1 = Map(50, 50)
scene1.walls = []
##############################Scene 2: Misc1####################################
scene2 = Map(50, 50)
scene2.walls = [[10, 30, 5, 10], [20, 10, 3, 30], [30, 0, 5, 48]]
##############################Scene 3: Misc1####################################
scene3 = Map(50, 50)
scene3.walls = [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]]
##############################Scene 4: Misc1####################################
scene4 = Map(50, 50)
scene4.walls = [[20, 0, 20, 2], [20, 2, 2, 43], [20, 48, 20, 2], [38, 5, 2, 43], [42, 0, 2, 45]]


switch_map = {
    '1': scene1,
    '2': scene2,
    '3': scene3,
    '4': scene4
}
