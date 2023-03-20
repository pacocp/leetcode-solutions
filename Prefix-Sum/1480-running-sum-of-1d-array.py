class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1d = [sum(nums[:i]) for i in range(1,len(nums)+1, 1)]
        return sum1d
