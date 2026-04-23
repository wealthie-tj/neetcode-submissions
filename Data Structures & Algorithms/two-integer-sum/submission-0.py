class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int] = {}
        for i,num in enumerate(nums):
            if seen.get(num, -1) == -1:
                seen[target - num] = i
            else:
                return [seen[num], i]