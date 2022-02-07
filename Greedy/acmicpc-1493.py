#백준 1493 박스 채우기 (Greedy)
l,w,h = map(int, input().split())
N= int(input())
cube=[]
for _ in range(N):
    cube.append(list(map(int, input().split())))
#큐브 한 변의 최대길이 (log N)
maximum=N-1
ans=0
# while True:
#     if min(l,w,h) >= 2**(maximum):

    