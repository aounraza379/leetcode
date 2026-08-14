# 1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == ' ':
                if count>0:
                    return count
            else:
                count = count+1
        return count

# Time: O(n) worst case
# Space: O(1)

# 2)
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         word = s.split()
#         count = len(word[-1])
#         return count

# Time: O(n)
# Space: O(n)