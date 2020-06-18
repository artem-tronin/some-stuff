c = 0
arr = []
for j in range(1, 22):
    for i in range(1, 10):

            arr.append(int(str(i) * j))

inpts = []
ans = []
for i in range(1, 1000):
    for j in range(len(arr)):
        # if len(set(num)) == 1:
        res = arr[j]%i
        if res == 0:
            jstr = str(arr[j])
            pow = int(arr[j]/i)
            if i*pow == arr[j]:
                print(i, '*', pow)
                inpts.append(i)
                subarr = [int(jstr[0]), len(jstr)]
                ans.append(subarr)
                c += 1
            break

print('\n', c)
print(inpts)
print(ans)
print()
ind = inpts.index(44)
print(ind)
print(ans[ind])