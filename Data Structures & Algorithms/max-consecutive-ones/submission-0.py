class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i, num in enumerate(nums):
            if num == 0:
                maxCount = max(maxCount, count)
                count = 0
            else: 
                count += 1

        return max(maxCount, count)
        