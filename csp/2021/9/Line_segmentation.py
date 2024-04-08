n = int(input())
nums = [0]+list(map(int,input().split()))+[0]
point = {}
max_ = 0
for id, value in enumerate(nums):
    if not value:
        continue
    max_ = max(max_, value)
    if value not in point:
        point[value] = [id]
    else:
        point[value].append(id)
island = [0]*(n+2)
temp = 0
top = 0
for data in range(max_, 0, -1):
    if data not in point:
        continue
    for i in point[data]:
        if island[i-1] == 0 and island[i+1] == 0:
            top += 1
        elif island[i-1] == 1 and island[i+1] == 1:
            top -= 1
        island[i] = 1
    temp = max(top,temp)
print(temp)


