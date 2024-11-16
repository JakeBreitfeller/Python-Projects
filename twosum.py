# My solution for leet code 2 sum in python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for x in range(len(nums)):
            for y in range(x):
                if (nums[y] + nums[x] == target):
                    return y,x
 
