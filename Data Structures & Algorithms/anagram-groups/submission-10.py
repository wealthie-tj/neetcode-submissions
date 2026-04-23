class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalOutput = []
        invalids = []

        for i in range(len(strs)):
            foundAnagrams = []
            if strs[i] in invalids:
                continue
            else:
                foundAnagrams.append(strs[i])
            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    foundAnagrams.append(strs[j])
                    invalids.append(strs[j])
            finalOutput.append(foundAnagrams)

        return finalOutput
