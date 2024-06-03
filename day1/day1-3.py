def pt(i,n):
    if i>=n:
        print("base")
        return
    print("Ending",i)
    for j in range(1,i):
        print(j)
    pt(i+1,n)
    print("Stratingline",i)
pt(1,8)
