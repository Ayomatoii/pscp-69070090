"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())

total = 0

for i in range(a, b + 1):
    if i % d == r:
        total += 1

print(total)
