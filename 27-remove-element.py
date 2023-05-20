class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        if j == -1: return 0
        while i < j:
            if nums[i] == val and nums[j] != val:
                aux = nums[i]
                nums[i] = nums[j]
                nums[j] = aux
                j -= 1
                i += 1
            elif nums[j] == val:
                j -= 1
            else:
                i += 1
        
        return j if nums[j] == val else j+1
