class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
      
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
           
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
    
        nums[i+1:] = reversed(nums[i+1:])

    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        
     
        for _ in range(1, k):
            self.nextPermutation(nums)
            
        return "".join(map(str, nums))