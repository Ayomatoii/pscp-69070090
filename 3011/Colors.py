"""Colors"""
colors_1 = input()
colors_2 = input()
if (colors_1 == "Red" and colors_2 == "Yellow") or (colors_2 == "Red" and colors_1 == "Yellow"):
    print ("Orange")
elif (colors_1 == "Red" and colors_2 == "Blue") or (colors_2 == "Red" and colors_1 == "Blue"):
    print ("Violet")
elif (colors_1 == "Blue" and colors_2 == "Yellow") or (colors_2 == "Blue" and colors_1 == "Yellow"):
    print ("Green")
elif (colors_1 == "Red" and colors_2 == "Red"):
    print ("Red")
elif (colors_1 == "Blue" and colors_2 == "Blue"):
    print ("Blue")
elif (colors_1 == "Yellow" and colors_2 == "Yellow"):
    print ("Yellow")
else :
    print ("Error")
