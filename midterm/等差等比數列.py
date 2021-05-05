s=int(input("請輸入資料"))
n=[[] for i in range(s)]
for i in range(s):
    for x in range(4):
        d=int(input(f"請輸入數字{i+1}"))
        n[i].append(d)
    print(n)

for z in range(len(n)):
    for j in range(3):
        dd=n[z][1]-n[z][0]
        rr=n[z][j+1]-n[z][j]
        if dd != rr:
            dd = n[z][1] / n[z][0]
            rr = n[z][j+1] / n[z][j]
            if dd == rr and j ==2 :
                for j in n[z]:
                    print(j,end=" ")
                print(int(n[z][3]*dd))
                print("等比")
        elif j ==2 :
            for j in n[z]:
                print(j,end=" ")
            print(int(n[z][3]+dd))
            print("等差")
        

