perfect_num = {6 : "6 = 1 + 2 + 3",
               28 : "28 = 1 + 2 + 4 + 7 + 14",
               496: "496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248",
               8128 : "8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064"}

num = int(input())
while num != -1:
    if num in perfect_num:
        print(perfect_num[num])
    else:
        print("%s is NOT perfect." % (num))
    num = int(input())