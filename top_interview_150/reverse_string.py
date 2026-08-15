class Solution:
    def reverseString(self, s: List[str]) -> None:
        end = len(s)-1
        l, r = 0, end

        while l<=r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
# Time: O(n)
# Space: O(1)