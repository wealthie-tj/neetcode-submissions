class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stack: Dict[int] = {}
        shortest = []
        longest = []

        if len(s) > len(t):
            shortest = t
            longest = s
        else:
            shortest = s
            longest = t

        for c in shortest:
            stack[c] = stack.get(c, 0) + 1 
        
        for c in longest:
            stack[c] = stack.get(c, 0) - 1
            if stack[c] < 0:
                return False
        
        return True