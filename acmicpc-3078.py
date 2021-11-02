#백준 3078번 좋은 친구(queue)
from collections import deque

N, K = map(int, input().split()) 

name=[]
for _ in range(N):
    name.append(len(input()))

queueList=[0,0]
for i in range(2,21):
    queueList.append(deque())


answer=0

for i in range(N):

    #비교할 queue
    long = name[i]
    queue = queueList[long]
 
    
    #queue에 이미 있으면 비교 후 apppend / pop&queue 길이만큼 +answer
    if len(queue) !=0:
        

        while len(queue)>0  and i - queue[0] > K:
            queue.popleft()
            answer+=len(queue)
            

        queue.append(i)
        

    else:
        queue.append(i)


#한 바퀴 다돌리고 queue에 남은 애들은 전부 좋은 친구다
for i in range(2,21):
    queue = queueList[i]
    pair = len(queue)
    
    if pair >1 :
        while pair>0 :
            pair-=1
            answer+=pair
            
    
print(answer)