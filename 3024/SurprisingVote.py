"""input"""
sum_s = float(input())
max_s = float(input())
min_s = 0
if max_s * 2 <= sum_s:
    min_s = sum_s - 2 * max_s
if max_s - min_s > 2:
    print("Surprising")
else:
    print("Not surprising")
