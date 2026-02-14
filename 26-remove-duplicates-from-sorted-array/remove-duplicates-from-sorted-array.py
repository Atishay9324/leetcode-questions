class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sorted = [nums[0]]
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                sorted.append(nums[i])
                k +=1
            else:
                continue
        nums[:k] = sorted
        return k