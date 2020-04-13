import sys
def rec(rl,i):
    res = rl[i]
    i+=1
    if i < len(rl):
        res = res + rec(rl,i)
    else:
        pass
    return res

rl = range(10)
i = 0
print(rec(rl,i))



INPUTDATA = "11\n1 1 1 1 1 1 1 1 1 1 1"
inp = INPUTDATA.split("\n")
N = int(inp[0])
times = list(map(int, inp[1].split(" ")))
i = 0
if (N % 2) == 0:
    i = int(N/2)
else:
    i = int(N/2)
s1 = 0
for idx in range(N):
    if idx > i:
        break
    s1 += times[idx]
i += 2
res = s1
while True:
    if i > N-2:
        res += s1+times[N-2]
        break
    s1 = s1 + times[i] + times[i-1]
    res += s1
    i+=2
print(res)
   
