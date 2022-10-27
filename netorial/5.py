#!/bin/python3

from heapq import heappop, heappush
import math
import os
import random
import re
import sys



#
# Complete the 'minCostPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. WEIGHTED_INTEGER_GRAPH g
#  2. INTEGER x
#  3. INTEGER y
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    G = [[] for _ in range(g_nodes+1)]
    for i in range(len(g_from)):
        u,v,w = g_from[i], g_to[i], g_weight[i]
        G[u].append([v,w])
        G[v].append([u,w])
    
    def getDeik(start, end):
        dist =[ float('inf') for _ in range(g_nodes+1)]
        # print(dist)
        # print(start)
        
        dist[start]=0
        heap = []
        heappush(heap,[0,start])
        while heap:
            cost, node = heappop(heap)
            if dist[node]<cost:
                continue
            if node == end:
                break
            for next, weight in G[node]:
                if dist[next]> cost+weight:
                    dist[next] = cost+ weight
                    heappush(heap, [ dist[next],next])
        
        return dist[end]
    dX = getDeik(1,x)
    dY = getDeik(x,y)
    dE = getDeik(y,g_nodes)
    answer = dX+dY+dE

    return answer
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     g_nodes, g_edges = map(int, input().rstrip().split())

#     g_from = [0] * g_edges
#     g_to = [0] * g_edges
#     g_weight = [0] * g_edges

#     for i in range(g_edges):
#         g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

#     x = int(input().strip())

#     y = int(input().strip())

#     result = minCostPath(g_nodes, g_from, g_to, g_weight, x, y)

#     fptr.write(str(result) + '\n')

#     fptr.close()
minCostPath(4 ,[1, 1, 2, 2, 3], [2, 4, 4, 3, 4], [6, 9, 10, 6, 11], 2 ,3)