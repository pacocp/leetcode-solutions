class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0
        pivot_index = 1
        while pivot_index < len(nums):
            if sum(nums[:pivot_index]) == sum(nums[pivot_index+1:]):
                return pivot_index
            pivot_index += 1
        
        return -1
