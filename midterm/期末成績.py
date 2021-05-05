a=[ ]
b=['國文','英文','微積分','體育','程式設計']
for i in range(5):
    c=input(f"請輸入{b[i]}")
    a.append(c)
print((int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4]))/5)
s=a.index(max(a))
s1=a.index(min(a))
print("最高分科目:",b[s],max(a))
print("最低分科目:",b[s1],min(a))