class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >=0:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i-=1
            else:
                i -=1


        