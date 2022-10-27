#개미굴
# sol 220902 
# dict or Trie

# N = int(input())
# tree={}
# for _ in range(N):
#     l = list(input().split())
#     M = int(l[0])
    
#     copyTree = tree
 
#     for i in range(1,M+1):
#         food = l[i]
#         if i==1:
#             if food not in copyTree:
#                 copyTree[food] = {}
                
#             copyTree = copyTree[food]
#             continue
        
#         if food not in copyTree:
#             copyTree[food] = {}
#         copyTree = copyTree[food]
# def DFS(d,level):        
#     for key, value in sorted(d.items()):
#         print('--'*level + key)
#         DFS(value,level+1)

# DFS(tree,0)
    
###Trie
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, dataList):
        current_node = self.root
        for data in dataList:
            if data not in current_node:
                current_node[data] = {}
            current_node = current_node[data]
        
            
    def travle(self,level, current_node):
        if current_node == {}:
            return
        

        current_node_list = sorted(current_node)
        for node in current_node_list:
            print('--'*level + node)
            self.travle(level+1, current_node[node])
            
N = int(input())
trie = Trie()
for _ in range(N):
    l = list(input().split())
    trie.insert(l[1:])

trie.travle(0, trie.root)


 
        
    
