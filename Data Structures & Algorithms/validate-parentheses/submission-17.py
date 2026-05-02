class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if pairs[char] != stack.pop():
                    return False

        if len(stack) > 0:
            return False
        return True
