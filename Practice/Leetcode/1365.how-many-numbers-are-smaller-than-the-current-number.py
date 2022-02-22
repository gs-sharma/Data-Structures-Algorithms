#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        
        count = {}
        #1 Sort the array 
        #2 Store in dictionary
        for i,v in enumerate(sorted(nums)):
            if v not in count:
                count[v] = i 
        
        #3 Taverse input and print result in same order
        return [count[v] for v in nums]

        
        
# @lc code=end

