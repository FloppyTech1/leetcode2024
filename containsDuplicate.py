# Key idea
# Create a dictionary and iterate over the array whilst appending each integer to the dictionary for a first time. Then, if it appears for a second time, return true.

class Solution(object):
    def containsDuplicate(self, nums):
        emptyDict = {} # Creation of empty dictionary
        for i in range(len(nums)): # Loop over the nums array
            if nums[i] in emptyDict: # If the integer is in the dictionary
                return True # Return true as it is the second time we find it
            else:
                emptyDict[nums[i]] = 1 # Otherwise, append it to the dictionary for the first time.
