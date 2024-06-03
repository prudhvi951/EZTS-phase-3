def pt(p):
    print("Leave Here",p)
    if p == 0:
        print("Base")
        return
    if p%2 == 1:
        print("Even pos",p)
    else:
        print("Odd pos:",p)
    pt(p-1)
    for i in range(p,-1,-1):
        print(i)
    print("entering here",p)
pt(11)
