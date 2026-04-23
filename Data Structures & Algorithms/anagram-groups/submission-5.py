class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i, string in enumerate(strs):
            alphabetList = [0 for _ in range(26)]
            print(string)
            for char in string:
                index = ord(char) - ord('a')
                alphabetList[index] += 1
                print(index)
            print(alphabetList)
            key = tuple(alphabetList)
            print(key)
            result[key] = result.get(key, []) + [string]
        
        return list(result.values())
        