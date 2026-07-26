"""input"""
tem = float(input())
tem1 = input()
tem2 = input()
if tem1 == "C" and tem2 == "K":
    tem = tem + 273.15
elif tem1 == "C" and tem2 == "F":
    tem = ((tem * 9 )/5) + 32
elif tem1 == "C" and tem2 == "R":
    tem = (tem + 273.15) * 9 / 5
elif tem1 == "K" and tem2 == "C":
    tem = tem - 273.15
elif tem1 == "K" and tem2 == "F":
    tem = (((tem - 273.15) * 9)/5) + 32
elif tem1 == "K" and tem2 == "R":
    tem = (tem * 9)/5
elif tem1 == "F" and tem2 == "C":
    tem = (tem - 32) * 5 / 9
elif tem1 == "F" and tem2 == "K":
    tem = ((tem -32) * (5/9)) + 273.15
elif tem1 == "F" and tem2 == "R":
    tem = (((tem - 32) * (5/9)) + 273.15) * 9 / 5
elif tem1 == "R" and tem2 == "C":
    tem = tem * 5 / 9 -273.15
elif tem1 == "R" and tem2 == "K":
    tem = tem * 5 / 9
elif tem1 == "R" and tem2 == "F":
    tem = (tem * 5 / 9 - 273.15) * 9 / 5 + 32
print(f"{tem:.2f}")
