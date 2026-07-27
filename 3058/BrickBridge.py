"""input"""
a = int(input())
b = int(input())
goal = int(input())

b = min(b, goal//5)
a_used = goal - (b * 5)

if a >= a_used:
    print(a_used)
elif a < a_used:
    print(-1)
