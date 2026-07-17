"""input"""
N = int(input())
line = 0
y = 1
z = 1
for i in range(1, N):
    if i == y:
        line += 1
        y += z + 2
        z += 2
if line % 2 == 1:
    if not N % 2:
        print(line * 2)
    elif N % 2 == 1:
        print(line * 2 - 1)
elif not line % 2:
    if not N % 2:
        print(line * 2 - 1)
    elif N % 2 == 1:
        print(line * 2)
