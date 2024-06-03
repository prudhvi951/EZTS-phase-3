def pn(n,i=1):
    if i>n:
        return
    print(i)
    pn(n,i+1)
pn(4)
