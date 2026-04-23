class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        stack: Dict[int] = {}

        for c in s:
            stack[c] = stack.get(c, 0) + 1 
        
        for c in t:
            stack[c] = stack.get(c, 0) - 1
            if stack[c] < 0:
                return False
        
        return True