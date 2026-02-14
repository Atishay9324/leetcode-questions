class Solution:
    def check(self, nums: List[int]) -> bool:
        k = 0
        if nums[-1]>nums[0]:
            k = k +1
        if len(nums) == 1 or len(nums) == 2:
            return True
        else:
            for i in range (1,len(nums)):
                if nums[i-1] > nums[i]:
                    k = k +1
        if k >1:
            return False
        else:
            return True
                