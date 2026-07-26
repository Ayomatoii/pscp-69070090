"""input"""
m = int(input())
d = int(input())
if 3 > m >= 1:
    print("winter")
elif 0 < d < 21 and m == 3:
    print("winter")
elif d >= 21 and m == 3:
    print("spring")
elif 0 < d < 21 and m == 6:
    print("spring")
elif 6 > m >= 4:
    print("spring")
elif d >= 21 and m == 6:
    print("summer")
elif 0 < d < 21 and m == 9:
    print("summer")
elif 9 > m >= 7:
    print("summer")
elif d >= 21 and m == 9:
    print("fall")
elif 0 < d < 21 and m == 12:
    print("fall")
elif 12 > m >= 10:
    print("fall")
elif d >= 21 and m == 12:
    print("winter")
