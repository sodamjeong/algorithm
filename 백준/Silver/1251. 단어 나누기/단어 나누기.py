word = input()
words = []
for i in range(1,len(word)):
    a = word[:i][::-1]
    for j in range(i, len(word)-1):
        b = word[i:j+1][::-1]
        c = word[j+1:][::-1]
        words.append(a+b+c)
print(sorted(words)[0])