#백준 2164번 카드2 (queue)
que = []
for i in range(0, int(input())):
    que.append(i+1)


while len(que) > 1:
    if len(que) % 2 == 0:
        que = que[1::2]
    else:
        tail= que[1]
        que = que[3::2]
        que.append(tail)
        
print(que[0])
