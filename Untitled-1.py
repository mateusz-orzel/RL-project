print("hello")
f = "hello"
d_f = {}
for x in f:
    if x in d_f.keys():
        d_f[x] += 1
    else:
        d_f[x]=1