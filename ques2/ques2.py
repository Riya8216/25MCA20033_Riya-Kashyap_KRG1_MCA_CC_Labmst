class Solution(object):
    def minimumSize(self, nums, maxOperations):
        lowest=1
        highest=max(nums)
        penalty=highest
        while lowest<=highest:
            mid=lowest+(highest-lowest)//2
            operations=0
            for x in nums:
                operations+=(x-1)//mid
            if operations<=maxOperations:
                penalty=mid
                highest=mid-1
            else:
                lowest=mid+1
        return penalty                
          
        
        

