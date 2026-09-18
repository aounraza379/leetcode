class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            result = []
            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])  
            result.extend(right[j:])    
            
            return result

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            
            return merge(left, right)
        return mergeSort(nums)

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# QUICK SORT
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)

        left = []
        middle = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)

        return self.sortArray(left) + middle + self.sortArray(right)

# Time Complexity
# Average case: O(n log n)
# Worst case: O(n^2)

# Space Complexity
# O(n)