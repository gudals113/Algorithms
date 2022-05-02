from collections import deque


def solution(people, limit):
    people.sort(reverse=True)
    q=deque(people)
    boat=[]
    
    while q:
        person = q.popleft()
        
        
        if boat==[]:
            boat.append([person,1])
            
        else:
            s,e=-1, len(boat)
            idx=-1
            while e-s>1:
                mid = (s+e)//2
                
                if limit - boat[mid][0] >=person and boat[mid][1]<2:
                    idx=mid
                    e=mid
                else:
                    s=mid
                    
            if idx==-1:
                boat.append([person,1])
            else:
                boat[idx][0]+=person
                boat[idx][1]+=1
                
        boat.sort(reverse=True)
        
    return len(boat)

ans = solution([50,40,40,45],70)
print(ans)