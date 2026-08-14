# 1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        current_element = None

        for num in nums:
            if count == 0:
                current_element = num
            
            if num == current_element:
                count += 1
            else:
                count -= 1
        return current_element 
        
# Time: O(n)
# Extra space: O(1)

# 2)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         length = len(nums)
#         return(nums[length//2])

# Time: O(n log n)
# Extra space: O(1)