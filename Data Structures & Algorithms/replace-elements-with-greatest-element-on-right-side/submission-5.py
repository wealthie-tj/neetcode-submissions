class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            greatest = 0
            if i == n-1:
                arr[i] = -1
                break
            for j in range(i+1, n):
                if arr[j] > greatest:
                    greatest = arr[j]
            arr[i] = greatest
        
        return arr