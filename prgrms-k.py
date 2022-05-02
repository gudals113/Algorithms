def solution(n,k):
    
    candidate = []
    strN = ''
    answer = 0
    maxNum = 0
    
    while n : 
        new = str(n%k)
        
        if new == '0' :
            if len(strN)==0 or strN=='1':
                strN = ''
                
            else:
                new = int(strN)
                maxNum=max(maxNum, new)
                candidate.append(new)
                strN = ''        
        else:
            strN =  new + strN
        n = n//k
    
    if len(strN)>0 and strN!='1':
        new = int(strN)
        maxNum=max(maxNum, new)
        candidate.append(new)
    
    isPrime=[1 for _ in range(maxNum+2)]
    isPrime[1]=0
    
    for i in range(2,maxNum+1):
        if isPrime[i] == 1:
            j=2
            while i*j < maxNum+1:
                isPrime[i*j]=0
                j+=1
                
    for i in range(len(candidate)):
        if isPrime[candidate[i]]==1:
            answer+=1
    
    return answer