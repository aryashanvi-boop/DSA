class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq=[0]*101
        for num in nums:
            freq[num]+=1
        ans=[]
        for num in nums:
            count=0
            for smaller in range(num):
                count+=freq[smaller]
            ans.append(count)
        return ans 
