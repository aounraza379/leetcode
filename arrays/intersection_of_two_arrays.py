class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        for i in nums1:
            if (i in nums2) and (i not in common):
                common.append(i)

        return common

# Time Complexity: O(n × m + n × k)
# Space Complexity: O(k)