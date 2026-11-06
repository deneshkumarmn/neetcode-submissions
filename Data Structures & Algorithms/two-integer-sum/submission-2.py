class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i,n in enumerate(nums):
            a = target - n
            if a in temp:
                return i,temp[a]
            temp[a] = i
        
                  
        