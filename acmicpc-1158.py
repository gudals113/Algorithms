#백준 1158번 요세푸스 문제 (linked list)
    ##1 linked list이용해서 풀기 가능한가?
# N, K = map(int, input().split()) 
# link=[]
# for i in range(1, N):
#     node = [i,i+1]
#     link.append(node)

# answer='<'

# link.append([N,1])

# current=0
# while True:
#     if len(link)==1:
#         answer= answer+ link[0][0]+'>'
#         break

#     for _ in range(K-1):
#         node=link[current]

    ##2 그냥 list만 사용해서 풀기
N, K = map(int, input().split()) 

link=[]
for i in range(1, N+1):
    link.append(i)

answer='<'
current=0
while True:
    if len(link)==1:
        answer= answer+ str(link[0])+'>'
        break

    
    current = (current+K-1)% len(link) 
    
    
    answer= answer+str(link.pop(current))+', '
print(answer)