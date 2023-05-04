tmp=[input().split() for _ in range(20)]
#01
score={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
cnt=0
ans=0
for i in tmp:
	#02
    if i[2]!="P":
        i[1]=float(i[1])
        ans+=score[i[2]]*i[1]
        cnt+=i[1]
#03
print("{:.6f}".format(ans/cnt))