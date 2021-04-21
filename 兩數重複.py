c=int(input("請輸入第一行正整數:"))
b=input("請輸入第二行數列:")
x=b.split(" ")
bignum=0
y=0

for i,num in enumerate(x):
    for l,checknum in enumerate(x):
        if i !=l:
            if int(num) == int(checknum):
                if int(num)> bignum:
                    bignum=int(num)

for num in x:
    if bignum ==int(num):
        y+=1
if bignum ==0:
    print("每個數字剛好只出現一次")
    
print("最大出現的數字為:",bignum)
print("出現次數:",y)



    

    
