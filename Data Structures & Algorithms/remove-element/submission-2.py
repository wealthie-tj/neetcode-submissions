class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        emptySpots = []
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] == val:
                emptySpots.append(i)
                k+=1
            if nums[i] != val and len(emptySpots) > 0:
                emptySpot = emptySpots.pop(0)
                print(emptySpot)
                nums[emptySpot] = nums[i]
                nums[i] = 0
                emptySpots.append(i)
            i+=1

        return len(nums) - k