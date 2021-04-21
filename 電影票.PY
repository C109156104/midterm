a=int(input("請輸入組數"))
b=[]
for i in range(a):
    tm=input(f"第{i+1}組:")
    c=tm.split(" ")
    b.append(c)

for i in b:
    print(int(i[0])*250+int(i[1])*175)
    

