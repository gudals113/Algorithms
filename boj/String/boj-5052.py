# boj-5052.py 전화번호 목록 문자열, 트라이로도 풀 수 있다네
 #220706 sol

T=int(input())
for _ in range(T):
    N = int(input())
    L = []
    for _ in range(N):
        l = input()
        L.append( [len(l), l] )
        
    L.sort(key=lambda x :x[0])
    
    def check():
        checkDict={}
        for i in range(N):
            num = L[i][1]
            tmp=''
            for j in range(len(num)):
                tmp+=num[j]
        
                if tmp in checkDict:
                
                    return 'NO'
            
            
            checkDict[num]=1

        return 'YES'
    
    print(check())
    
