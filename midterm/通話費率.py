import math
a=int(input("請輸入月租費:"))
b=int(input("請輸入通話時間:"))
if a <=186:
    b*=0.09
    b1=b/186
    if b1 <=1:
        b*=0.9
    else:
        b*=0.8
elif a<=386:
    b*=0.08
    b1=b/386
    if b <=1:
        b*=0.8
    else:
        b*=0.7
elif a<=586:
    b*=0.07
    b1=b/586
    if b <=1:
        b*=0.7
    else:
        b*=0.6
elif a<=986:
    b*=0.06
    b1=b/986
    if b <=1:
        b*=0.6
    else:
        b*=0.5
print("通話費為",round(b))
    