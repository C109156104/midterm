n=int(input("請輸入整數:"))
if n%2 == 0 and n%11 ==0:
    if n%5 != 0 and n%7 !=0:
        print("Yes")
    else:
        print("No")