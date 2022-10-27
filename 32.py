from collections import defaultdict, deque
from heapq import heappop, heappush


def solution(k):
    d = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6 }    
    q= deque()

    heap = [[0, '']]
    
    answer={}
    visited={}
    while heap:
        used, word= heappop(heap)
        
        if used>k:
            continue
        
        if used==k:
            if len(word)>1 and word[0]=='0':
                pass
            else:
                answer[word]=1        
            continue
        
        for plusword, count in d.items():

            if count+used>k:
                continue
            
            if word+plusword not in visited:
                visited[word+plusword]=1
                heappush(heap,[used+count, word+plusword])
    
    print(len(answer))
    return len(answer)     

solution(11)        

