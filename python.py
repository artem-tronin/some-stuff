# a=int(input())
# b=int(input())
ar=[]
for i in range(20000):
    s=True
    for j in str(i):
        if int(j)%2!=0:
            if s:
                s=False
            else:
                s=True
    if not s:
        print(i)
        ar.append(i)
print(ar)
