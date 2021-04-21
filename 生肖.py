#可用list寫簡便
n=int(input("請輸入年份"))
if n%12==0:
    print("momkey")
elif n%12 ==1:
    print("rooster")
elif n%12 ==2:
    print("dog")
elif n%12 ==3:
    print("pig")
elif n%12 ==4:
    print("rat")
elif n%12 ==5:
    print("ox")
elif n%12 ==6:
    print("tiger")
elif n%12 ==7:
    print("rabbit")
elif n%12 ==8:
    print("dragon")
elif n%12 ==9:
    print("snake")
elif n%12 ==10:
    print("horse")
else:
    print("sheep")