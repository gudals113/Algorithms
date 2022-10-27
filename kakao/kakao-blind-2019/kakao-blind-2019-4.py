# kakao-blind-2019-4.py

import sys
sys.setrecursionlimit(10**5)
def solution(nodeinfo):
    N = len(nodeinfo)
    tree = [[-1,-1] for _ in range(N) ]
    nodeDict = {}
    
    for i in range(N):
        nodeinfo[i].append(i)
        nodeDict[i] = nodeinfo[i]
    
    nodeinfo.sort(key=lambda x:(-x[1],x[0]))
    root =  nodeinfo[0][2] 
    
    level = []
    tmp = [root]
    for i in range(1,N):
        x,y,node =  nodeinfo[i]
        bx,by,bnode = nodeinfo[i-1]
        if by!=y :
            level.append(tmp)
            tmp = [node]
        else:
            tmp.append(node)
    level.append(tmp)

    def insert(node, level, target, target_level):

        if level+1==target_level:
            if nodeDict[node][0] > nodeDict[target][0]:
                tree[node][0] = target
            else:
                tree[node][1] = target    
                
            return
        
        left,right  = tree[node]
        
        if nodeDict[node][0] > nodeDict[target][0] :
            insert(left,level+1, target,target_level)
        else:
            insert(right,level+1, target, target_level)


    for l in range(1,len(level)):
        for n in level[l]:
            insert(root, 0, n, l)
    
    preList = []        
    def pre(node):
        left,right = tree[node][0], tree[node][1]
        preList.append(node+1)
        if left != -1 :
            pre(left)
        if right!= -1:
            pre(right)
    postList = []
    def post(node):
        left,right = tree[node][0], tree[node][1]
        
        if left!=-1 :
            post(left)
        if right!=-1:
            post(right)    

        postList.append(node+1)
      
    pre(root)
    post(root)
    answer = [preList,postList]    
    
    return answer


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	)