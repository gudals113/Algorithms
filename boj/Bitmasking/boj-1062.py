#가르침 bitmasking + backtracking 220504
# 백트래킹만 이용해서 풀 수 있다. 비트마스킹으로 풀면 시간 좀 줄어든다.

N,K = map(int,input().split())
# alpha = [0 for _ in range(26)]
alpha = 0

if K < 5:
    print(0)
    quit()

    #초기 세팅
K -= 5

alpha |= 1<<(ord('a')-97)
alpha |= 1<<(ord('c')-97)
alpha |= 1<<(ord('n')-97)
alpha |= 1<<(ord('t')-97)
alpha |= 1<<(ord('i')-97)
# .....gfedcba


wordList = []
for _ in range(N):
    word = input()
    word = word[4:-4]
    tmp = 0
    for i in range(len(word)):
        w = word[i]
        tmp |= 1<<(ord(w)-97)
    wordList.append(tmp)
    
    
def check():
    canRead = 0
    
    for word in wordList:
        if word & alpha == word:
            canRead+=1
        
    
    return canRead 
          
sol = 0
def DFS(idx, k) :
    global alpha,sol
    
    if idx == 26 or k==K:
        canRead = check()
        sol = max(sol, canRead)
        return
    
    for i in range(idx, 26) :
        if alpha & 1<<i == 0 :
            
            alpha |= 1<<i
            
            DFS(i,k+1)
            
            
            alpha&=  ~(1<<i)
            
DFS(0,0)
print(sol)

