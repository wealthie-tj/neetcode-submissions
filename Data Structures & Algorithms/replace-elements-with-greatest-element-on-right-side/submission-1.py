class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curGreatest = arr[-1]
        prevGreatest = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            curGreatest = max(arr[i], prevGreatest)
            arr[i] = prevGreatest
            prevGreatest = curGreatest
            
        
        return arr