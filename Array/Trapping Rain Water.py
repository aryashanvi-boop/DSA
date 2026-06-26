class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftmax=height[l]
        rightmax=height[r]
        water_level=0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                water_level+=leftmax-height[l]
            else:
                r-=1
                rightmax= max(rightmax,height[r])
                water_level+=rightmax-height[r]
        return water_level
