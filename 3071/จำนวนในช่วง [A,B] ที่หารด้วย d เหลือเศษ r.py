"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())

x = (b - r) // d - (a - 1 - r) // d

print(x)
