def movealldiscs(n,src,extra,dest):
    if n == 1:
        print("Move 1st disc from",src,"to",dest)
        return
    movealldiscs(n-1,src,dest,extra)
    print("Move",n,"the disc from",src,"to",dest)
    movealldiscs(n-1,extra,src,dest)
    
movealldiscs(3,"srorce","extraspace","destination")
