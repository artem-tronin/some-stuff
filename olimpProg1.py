a, b = map(int, input().split())

# for i in range(a,b+1):
#     if i%9==0:
#         print(i, end=' ')
def countDigits(num):
    num = str(num)
    sum = 0
    for i in num:
        sum += int(i)

    return sum

# ans = 0
flag = True
for i in range(a,b+1):
    if countDigits(i*2) == countDigits(i*3) == countDigits(i*4) == countDigits(i*5) == countDigits(i*6) == countDigits(i*7) == countDigits(i*8) == countDigits(i*9):
        flag = False
        print(i, end=' ')

if flag:
    print(0)
