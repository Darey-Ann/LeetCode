# 1480. Running Sum of 1d Array
# Time taken: 17 m 15 s

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        rsums = []
        
        for i in range (1,len(nums)+1):
            rsums.append(sum(nums[:i]))
        
        return rsums