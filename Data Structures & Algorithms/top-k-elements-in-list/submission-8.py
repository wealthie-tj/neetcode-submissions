class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # now we want to map frequency to number using bucket sort
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # we wanna go from the highest frequency and then go down -> this is indicated by -1 3rd param
        # and since no number will ever have 0 frequency, we do len(freq) - 1 and then stop before 0
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res
