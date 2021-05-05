x=int(input("請輸入x軸座標:"))
y=int(input("請輸入y軸座標:"))
sum=0
if x>0 and y>0:
    sum=(x-0)**2+(y-0)**2
    print("位於第一象限")
    print("離原點座標為根號",sum)
elif x<0 and y>0:
    sum=(x-0)**2+(y-0)**2
    print("位於第二象限")
    print("離原點座標為根號",sum)
elif x<0 and y<0:
    sum=(x-0)**2+(y-0)**2
    print("位於第三象限")
    print("離原點座標為根號",sum)
elif x>0 and y<0:
    sum=(x-0)**2+(y-0)**2
    print("位於第四象限")
    print("離原點座標為根號",sum)
elif x==0 and y>0:
    sum=(x-0)**2+(y-0)**2
    print("位於上半平面y軸上")
    print("離原點座標為根號",sum)
elif x==0 and y<0:
    sum=(x-0)**2+(y-0)**2
    print("位於下半平面y軸上")
    print("離原點座標為根號",sum)
elif x>0 and y==0:
    sum=(x-0)**2+(y-0)**2
    print("位於右半平面x軸上")
    print("離原點座標為根號",sum)
elif x<0 and y==0:
    sum=(x-0)**2+(y-0)**2
    print("位於左半平面x軸上")
    print("離原點座標為根號",sum)
else:
    print("位於原點")