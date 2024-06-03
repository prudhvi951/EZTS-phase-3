def pt(i,n):
    if i>=n:
        print("Base")
        return
    print("Hello",i)
    print("World",i)
    pt(i+1,n)
    print("This",i)
    print("Recursion",i)
pt(1,8)
