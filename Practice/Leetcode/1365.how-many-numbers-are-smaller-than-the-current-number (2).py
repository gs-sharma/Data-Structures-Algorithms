#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums):

        # Accourding to given constraint    
        count = [0]*101
        result = []        
        # Count Occurance
        for num in nums:
            count[num] +=1

        # prefix sum
        for i in range(1,101):
            count[i] += count[i-1]

        #Result
        for num in nums:
            if num > 0:
                result.append(count[num -1])
            else:
                result.append(0)

        return result
        

        
        
# @lc code=end

