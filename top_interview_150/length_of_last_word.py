class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        count = len(word[-1])
        return count