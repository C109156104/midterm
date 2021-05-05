a=input("請輸入搭乘幾次")
c=1
s=0
for i in range(int(a)):
    b=int(input(""))
    if c < b:
        s+=(b-c)*20
    else:
        s+=(c-b)*10
    c=b
print(s)