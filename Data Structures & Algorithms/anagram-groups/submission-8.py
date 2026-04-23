class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i, string in enumerate(strs):
            alphabetList = [0 for _ in range(26)]
            for char in string:
                index = ord(char) - ord('a')
                alphabetList[index] += 1
            key = ",".join(str(num) for num in alphabetList)
            result[key] = result.get(key, []) + [string]
        
        return list(result.values())
        