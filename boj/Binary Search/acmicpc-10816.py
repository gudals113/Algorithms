# N = int(input())
# card = list(map(int, input().split()))
# M= int(input())
# question = list(map(int, input().split()))
# card = sorted(card)


# answer=[0 for _ in range(M)]

# for i in range(M):
#     s ,t = 0, N-1 #이렇게 설정하면 된다. 10815와 비교
#     check = question[i]

#     while t>s:
#         mid = (s+t)//2
#         if check == card[mid]:
#             answer[i]=card[s:t+1].count(check)
#             break
#         elif check > card[mid] :
#             s,t= mid+1,t
#         elif check < card[mid]:
#             s,t= s,mid-1
                
# for i in range(M):
#     print(answer[i], end=' ')

N = int(input())
card = list(map(int, input().split()))
M= int(input())
question = list(map(int, input().split()))
card = sorted(card)
count=[1 for _ in range(N)]

dic={}
#해시맵에 총 몇개의 카드가 존재하는지 저장
for c in card:
    if c in dic:
        dic[c]+=1
    else:
        dic[c]=1

answer=[0 for _ in range(M)]
for i in range(M):
    s ,t = -1, N #이렇게 설정하면 된다. 10815와 비교
    check = question[i]

    while t-s>1:
        mid = (s+t)//2

        if check == card[mid]:
            answer[i]=dic[check] # 해시맵에 저장된 카드의 개수 불러오기
            break
        elif check > card[mid] :
            s,t= mid,t
        elif check < card[mid]:
            s,t= s,mid
                
for i in range(M):
    print(answer[i], end=' ')


