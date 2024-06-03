def maxnum(i,n,nums,m):
    if i == n-1:
        print(m)
        return 
    if nums[i]<m:
        m = nums[i]
    maxnum(i+1,n,nums,m)
def maxnum2(i,n,nums):
    if i == n - 1:
        return nums[n-1]
    c = maxnum2(i+1,n,nums)
    if c > nums[i]:
        return nums[i]
    return c
p = maxnum2(0,4,[1,2,3,4])
print(p)
maxnum(0,5,[1,5,4,2,3],min([1,5,4,2,3]))
