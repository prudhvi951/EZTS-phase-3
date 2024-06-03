def ssum(n,res):
    if n == 0:
        return res
    res = res+n
    return ssum(n-1,res)

n = int(input())
k = ssum(n,0)
print(k)
