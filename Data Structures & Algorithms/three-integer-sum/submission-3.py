class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        left = 0
        right = len(nums) - 1
        result = []
        
        n_sorted = []
        n_sorted = sorted(nums)

        for i in range(len(n_sorted)-2):
            if i > 0 and n_sorted[i] == n_sorted[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                total = n_sorted[i] + n_sorted[left] + n_sorted[right]
                if total == 0:
                    result.append([n_sorted[i], n_sorted[left], n_sorted[right]])

                    left += 1
                    right -= 1
                    while left < right and n_sorted[left] == n_sorted[left-1]:
                        left += 1

                    while left < right and n_sorted[right] == n_sorted[right+1]:
                        right -= 1                    
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                
        
        return result