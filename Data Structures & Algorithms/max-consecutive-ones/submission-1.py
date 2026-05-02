class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
                continue
            else:
                if temp >= counter:
                    counter = temp
                temp = 0
        
        if temp >= counter:
            counter = temp
            
        return counter
        