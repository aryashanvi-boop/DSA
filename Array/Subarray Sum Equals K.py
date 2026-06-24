class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
        ans=0
        prefix_sum=0
        freq={0:1}
        for num in nums:
            prefix_sum+=num
            need= prefix_sum - k
            if need in freq:
                ans+=freq[need]
            if prefix_sum in freq:
                freq[prefix_sum]+=1
            else:
                freq[prefix_sum]=1
        
        return ans
