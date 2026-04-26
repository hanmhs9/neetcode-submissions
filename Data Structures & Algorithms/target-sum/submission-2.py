class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        dp = {}

        def trackback(i, total):  
            if i == len(nums):
                return 1 if (total == target) else 0
            
            if (i,total) in dp:
                return dp[(i,total)]

            dp[(i, total)]= trackback(i+1, total+nums[i]) + trackback(i+1, total-nums[i])

            return dp[(i, total)]       
        
        return trackback(0, 0)