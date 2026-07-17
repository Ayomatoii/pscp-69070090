"""input"""
N = int(input())
ten = ""
for i in range(N, -1, -1):
    if not i % 10:
        ten = ten + str(i)
    if i and not i % 10:
        ten = ten + " "
print(ten)
