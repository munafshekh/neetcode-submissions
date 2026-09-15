class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
         for i in range(len(nums)):
            for x in range(i):
                if nums[x] == nums[i]:
                    return True
        
         return False