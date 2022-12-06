# 724. Find Pivot Index
# Time taken: 24 m 13 s

# Submitted at 21 without the break statement. For testcase [-1,-1,0,0,-1,-1] this returned index 3 instead of the expected index 2.

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pivotindex = -1

        for i in range (len(nums)):
            #print 'index '+str(i)
            #print 'left '+str(sum(nums[:i]))
            #print 'right '+str(sum(nums[i:])-nums[i])+'\n'
            if sum(nums[:i]) == sum(nums[i:])-nums[i]:
                pivotindex = i
                break # stops at the first pivot where the condition is true

        return pivotindex