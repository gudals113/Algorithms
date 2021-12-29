def dfs(graph, start, visited=None):
   if visited is None:
       visited = set()
   visited.add(start)

   print(start)

   for next in graph[start] - visited:
       dfs(graph, next, visited)
   return visited


graph = {'0': set(['1', '2']),
        '1': set(['0', '3', '4']),
        '2': set(['0']),
        '3': set(['1']),
        '4': set(['2', '3'])}

dfs(graph, '0')


#list 로 하는 법

# def dfs(graph, start_node):
#     visit = list()
#     stack = list()

#     stack.append(start_node)

#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])

#     return visit


# if __name__ == "__main__":
#     graph = {
#         'A': ['B'],
#         'B': ['A', 'C', 'H'],
#         'C': ['B', 'D'],
#         'D': ['C', 'E', 'G'],
#         'E': ['D', 'F'],
#         'F': ['E'],
#         'G': ['D'],
#         'H': ['B', 'I', 'J', 'M'],
#         'I': ['H'],
#         'J': ['H', 'K'],
#         'K': ['J', 'L'],
#         'L': ['K'],
#         'M': ['H']
#     }

#     print(dfs(graph, 'A'))