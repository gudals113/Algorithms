#  여행경로
from collections import defaultdict

def solution(tickets):
    answer = ['ICN']
    dict = defaultdict(list)
    visited= defaultdict(list)
    
    for t in tickets:
        u,v = t[0],t[1]
        
        dict[u].append(v)
        visited[u].append(0)
        
        dict[u].sort(reverse=True)
    
    def DFS(start,count):
        global sol
        if count==len(tickets) :
            sol= answer[:]
            return
        
        else:
            
            for i in range(len(dict[start])):
                if visited[start][i]==0:
                    visited[start][i]=1
                    answer.append(dict[start][i])
                    
                    DFS(dict[start][i],count+1)
                    visited[start][i]=0
                    answer.pop()
        
    DFS('ICN',0)
    
    return sol



# rst = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
rst1 = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(rst1)