class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1

        #so the height only matters of the lowest of the 2
        #the distance between the bars is the width [so indices are subtracted]

        highest = 0
        
        while left < right:
            total = (right-left) * min(heights[right], heights[left])
            if heights[left] < heights[right]:
                left +=1
                if total > highest:
                    highest = total
            else:
                right -=1
                if total > highest:
                    highest = total
            total = 0


        return highest




        