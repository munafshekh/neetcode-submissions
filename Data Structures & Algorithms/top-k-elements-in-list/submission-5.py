from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] +=1
        
        # [key, value] so [0,1]
        sorted_dict = sorted(counter, key=counter.get, reverse=True)
        
        return sorted_dict[0:k]
            
        
        



