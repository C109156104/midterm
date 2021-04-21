m={"A":14,"J":11,"Q":12,"K":13}
a=input("請輸入")
b=a.split(" ")
c=0
for i in b:
    if i.isdigit():
        c+=int(i)
    else:
        c+=m[i]
print(c)