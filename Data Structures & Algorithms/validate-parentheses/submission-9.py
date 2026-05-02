class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        opens = ['(', '{', '[']
        closes = [')', '}', ']']

        if len(s) == 1:
            return False

        for bracket in s:
            if bracket in opens:
                temp.append(bracket)
            else:
                if len(temp) == 0:
                    return False
                
                openBracket = temp.pop()
                
                if self.checkIfMatch(openBracket, bracket):
                    continue
                else:
                    return False
        
        if len(temp) != 0:
            return False 
    
        return True
    

    def checkIfMatch(self, openBracket: str, closeBracket: str):
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        return pairs.get(openBracket) == closeBracket