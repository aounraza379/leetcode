class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        common = ""

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common += first[i]
            else:
                break
        return common