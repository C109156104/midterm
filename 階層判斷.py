m=int(input("請輸入階層值:"))
s=1
i=1
while s <= m:
   i+=1 #多跑一次
   s*=i
print(i-1)
