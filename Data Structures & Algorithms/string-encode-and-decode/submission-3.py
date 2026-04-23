class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for curStr in strs:
            newStr = str(len(curStr)) + '#' + curStr
            result.append(newStr)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        length = ''
        index = 0
        while index < len(s):
            if s[index] == '#':
                string = s[index+1:index+int(length)+1]
                result.append(string)
                index = index + int(length)
                length = ''
            else:
                length = length + s[index]
            index+=1
        return result

                #'2#hi...'