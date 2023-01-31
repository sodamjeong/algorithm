n = [0,1]
for i in range(int(input())):
        n.append(n[i]+n[i+1])
print(n[-2])