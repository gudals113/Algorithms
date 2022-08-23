#부분수열의 합 2, meet in the middle, hint 220629
#1182번은 getDict 코드로만 해결이 가능하다.
from collections import defaultdict
N,S = map(int, input().split())
L = list(map(int, input().split()))
answer=0

def getDict(L):
    global answer
    dict = defaultdict(int)
    
    for i in range(len(L)):
        num = L[i]    
        candidate=defaultdict(int)
        candidate[num]=1

        for past in dict:
            candidate[num+past] += dict[past]    
    
        for c in candidate:   
            dict[c]+=candidate[c]
    
    # answer+= dict[S]
    if S in dict:
        answer+=dict[S]

    return sorted(dict.items())

left_dict = getDict(L[:N//2])
right_dict = getDict(L[N//2:])

l=0
r=len(right_dict)-1

while True:
    
    if l>=len(left_dict) or r <= -1 :
        break
    
    left_value ,right_value = left_dict[l][0],right_dict[r][0]
    left_num, right_num = left_dict[l][1], right_dict[r][1]
    
    # print(left_value, right_value)
    if left_value + right_value == S :
        answer+= left_num * right_num
        l+=1
        r-=1
    
    elif left_value + right_value < S or r==0:
        l+=1
        
    elif left_value + right_value > S or l== len(left_dict)-1 : 
        r-=1

print(answer)