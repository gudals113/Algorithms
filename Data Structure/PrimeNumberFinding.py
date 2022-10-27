# 소수 판별 알고리즘
import math
N = 779

# 1. O(N)
isPrime = True
for i in range(2,N):
    if N%i == 0 : isPrime = False
    
# 2. O(N) - N/2보다 큰 수로 나누었을 때 나머지 0은 불가능하다.
isPrime = True
for i in range(2,N//2+1):
    if N%i == 0 : isPrime = False
    

# 3. O(N**1/2) 가운데 약수까지만 확인하는 방법. 가운데 약수는 N의 제곱근에 위치한다.
isPrime = True
for i in range(2, int(math.sqrt(N))+1):
    if N%i == 0 : isPrime = False
    
# 4. O(N log(log N)) 에라토스테네스의 체 - 여러 개 소수 판별하기 위해 사용 
primeNum = [True for _ in range(N+1)]
for i in range(2, int(math.sqrt(N))+1):
    
    if primeNum[i] == True :    
        
        for j in range(2,N):
            if i*j > N :
                break
            
            primeNum[i*j]==False
            
    
    