from math import sqrt

def solution(n, k):
    answer = 0
    
    def changeToK(n,k):
        if k == 10:
            return str(n)
        tmp = ''
        while n>0:
            tmp = str(n%k) + tmp
            n = n//k
        return tmp
                    
    s = changeToK(n,k)
    def checkPrime(n):
        if n==1:
            return False
        isPrime = True
        for i in range(2, int(sqrt(n))+1):
            if n%i == 0 : isPrime = False
        return isPrime
    
    # maxNum = 10_000_000
    # primeList = [1 for _ in range(maxNum)]
    # primeList[0],primeList[1] = 0,0
    
    # for i in range(2,int(sqrt(maxNum))):
    #     if primeList[i]==1:
    #         idx=2
    #         while idx*i<1000001:
    #             primeList[idx*i]=0
    #             idx+=1
    
    
    tmp = ''
    for i in range(len(s)):
        if s[i]=='0':
            if len(tmp)>0 and checkPrime(int(tmp)):
                print(tmp)
                answer+=1
            tmp = ''
            
        else:
            tmp+=s[i]
    
    if len(tmp)>0 and checkPrime(int(tmp))==1:
        answer+=1
    
    return answer

solution(437674,3)
# solution(110011,	10)