# Child function to parent function
def findSum(index, nums, n):
	if index == n:
		return 0 
	nextEleSum = findSum(index + 1, nums, n)
	if nums[index] % 5 == 0:
		nextEleSum += nums[index] 
	return nextEleSum

# parent function to child function 
def findSum2(index, nums, n, result):
	if index == n:
		print("Sum is:", result)
		return 
	if nums[index] % 5 == 0:
		result += nums[index]
	findSum2(index + 1, nums, n, result)
	
	
	
	'''[10, 11, 12, 13, 14, 15]
	 0.  1.  2.   3.  4.  5 
	even indices: 0, 2, 4 
	odd indices: 1, 3, 5 '''
	
def printLeftToRight(index, nums, n):
	if index == n:
		return 
	
	if index % 2 == 0:
		print(nums[index])
	printLeftToRight(index + 1, nums, n)
	
def printLeftToRightBetterOne(index, nums, n):
	if index >= n:
		return 
	
	print(nums[index])
	printLeftToRightBetterOne(index + 2, nums, n)
	
def printRightToLeftBetterOne(index, nums, n):
	if index >= n:
		return 
	
	printLeftToRightBetterOne(index + 2, nums, n)
	print(nums[index])
printLeftToRight(0, nums, len(nums))



def printRightToLeftInReverseManner(index, nums, n):
	if index < 0:
		return 
	print(nums[index])
	printRightToLeftInReverseManner(index - 2, nums, n)
	
	
	
n = len(nums)
if n % 2 == 0:
	printRightToLeftInReverseManner(n - 2, nums, n)
else:
	printRightToLeftInReverseManner(n - 1, nums, n)
	


'''0, 2, 4, 6,
[10, 12, 13, 14, 15]
 0,  1,   2, 3, 4  ''' 


	
	
	
	
	
	
	
	
	
	
	
	
	
