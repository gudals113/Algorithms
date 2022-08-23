# boj-1701.py 
# Cubeditor , , try220707
from collections import defaultdict, deque
S = input()
N = len(S)

visited=[0 for _ in range(N)]
answer = 0

for i in range(N):
    if visited[i]:
        continue
    
    startWord = S[i]
    
    candidate = deque()
    
    #startWord 모두 후보군에 넣기
    for idx in range(i,N):
        if not visited[idx] and S[idx]==startWord :
            visited[idx]=1
            candidate.append(idx)
    
    d = 1
    while candidate:

        wordDict = defaultdict(list)
        
        while candidate:
            start = candidate.popleft()
            if start+d <= N :
                word = S[start:start+d]
                wordDict[word].append(start)
        
        # print(wordDict)
        for word in wordDict :
            if len(wordDict[word]) >=2 :
                l = wordDict[word]
                for j in l :
                    candidate.append(j)
                    visited[j+d-1]=1

        if candidate:
            d+=1

    answer = max(answer, d-1)   
    
print(answer)
        
    
        