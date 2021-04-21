list=['Capricorn','Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
list1=[101,121,219,321,421,522,622,723,824,924,1024,1122,1222]
list2=[120,218,320,420,521,621,722,823,923,1023,1121,1221,1230]
c=input("請輸入日期")
for i in range(13):
    if int(c) >= list1[i] and int(c) <=list2[i]:
        print(list[i])




