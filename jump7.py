a = 0
while a in range (0,100):
    a = a + 1
    if a % 7 == 0:
        continue
    elif a % 10 == 7:
        continue
    elif a // 10 == 7:
        continue
    else:
        print (a)
