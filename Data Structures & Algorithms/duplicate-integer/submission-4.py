class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            found = seen.get(num, -1) 
            if found == -1:
                seen[num] = 1
            else:
                return True
        return False