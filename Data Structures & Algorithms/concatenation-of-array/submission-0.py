class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * (len(nums)*2)
        for i, num in enumerate(nums):
            result[i] = num 
            result[i+len(nums)] = num
        print(result)
        return result
        