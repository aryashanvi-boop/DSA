class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxa=0
        for num in nums:
            if num==1:
                count=count+1
                maxa= max(maxa,count)
            else:
                count=0
        return maxa
        
