class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = maX = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num) 
            maX = max(maX, cur)
        return maX