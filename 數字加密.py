a=list(input("請輸入一串數字"))
b=""
for i in a:
    b=b+str((int(i)+7)%10)
b=b[2]+b[3]+b[0]+b[1]
print(b)