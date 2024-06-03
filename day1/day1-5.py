#Recurssion
def printsum(i,n,nums,res):
    if i == n:
        print("Sum is :",res)
        return
    res = res+nums[i]
    printsum(i+1,n,nums,res)
#Back Tracking
def newsum(i,n,nums):
    if i == n:
        return 0
    k = newsum(i+1,n,nums)
    return k + nums[i]
printsum(0,4,[1,2,3,4],0)
p = newsum(0,4,[1,2,3,4])
print(p)
