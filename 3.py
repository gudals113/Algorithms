from collections import defaultdict
from itertools import permutations


def solution(k):
    d = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6 }
    
    made = defaultdict(int)
    visited = {}
    def DFS(start,left):
        if left<0:
            return 
        
        if left == 0:
            # print(made)
            return

        for i in range(start,10):
            need = d[i]
            idx = 1
            while True:
                if idx*need>left:
                    break
                print(i, need, idx)
                made[i]+=idx
                DFS(start+1,left-need*idx)
                made[i]-=idx
                
                idx+=1
                     
    DFS(0,k)
    answer = len(visited)
    print(answer)
    return answer

solution(11)
