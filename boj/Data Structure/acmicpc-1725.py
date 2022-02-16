#백준 1918번 히스토그램 (stack)
N = int(input())
stack = []
answer = 0
histogram = []
for _ in range(N):
    histogram.append(int(input()))

for index in range(N):
    current = histogram[index]

    if stack == [] or histogram[stack[-1]] <= current:
        stack.append(index)

    elif histogram[stack[-1]] > current:

        while True:
            last = stack.pop()

            heigth = histogram[last]
            right = index

            if stack == []:
                left = 0
            else:
                left = stack[-1]+1

            extent = (right - left) * heigth
            answer = max(answer, extent)

            if stack == [] or histogram[stack[-1]] <= current:
                stack.append(index)
                break


right = N
rest = len(stack)
for _ in range(rest):
    last = stack.pop()
    heigth = histogram[last]
    if stack == []:
        left = 0
    else:
        left = stack[-1]+1

    extent = (right - left) * heigth
    answer = max(answer, extent)


print(answer)
