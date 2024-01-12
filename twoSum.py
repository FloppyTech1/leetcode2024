# Key idea
# Create a copy of our original nums array. Loop over the array and at each iteration find the max and min. If the current sum is > than our target, pop the current max. Same
# applies for <. If the sum is = to our target, we create a list containing all the indices and pairs the index with it's respective integer. If numMin or numMax are equal
# to x, we keep them in the list as one of the indices.

class Solution(object):
    def twoSum(self, nums, target):
        numsCopy = nums.copy()
        for i in range(0, len(nums)):
            numMin = min(nums)
            numMax = max(nums)
            currentSum = numMin + numMax
            if currentSum > target:
                nums.pop(nums.index(numMax))
            elif currentSum < target:
                nums.pop(nums.index(numMin))
            else:
                indices = [i for i, x in enumerate(numsCopy) if x == numMin or x == numMax]
                return indices
