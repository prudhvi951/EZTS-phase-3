def printBinary(size,result,n):
    if size == n:
        print(result)
        return
    printBinary(size+1,result+"1",n)
    printBinary(size+1,result+"0",n)

n = 4
printBinary(0,"",n)
