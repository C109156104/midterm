m=input("請輸入數值")
list1=list(m)
list2=list(m)
c=""
c1=""
n=len(list(m))
for i in range(n):
    for j in range(n-1):
        if list1[j]>list1[j+1]:
            tmp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=tmp
        if list2[j]<list2[j+1]:
            tmp=list2[j]
            list2[j]=list2[j+1]
            list2[j+1]=tmp
print(list1,list2)
for i in range(n):
    c= c+str(list1[i])
    c1=c1+str(list2[i])
print(int(c1)-int(c))


