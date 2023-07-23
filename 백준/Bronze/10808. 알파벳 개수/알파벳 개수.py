word = [0] * 26
for i in input():
    word[ord(i)-97] += 1
print(*word)