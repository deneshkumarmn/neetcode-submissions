class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {} #value: position

        for i,n in enumerate(nums):
            x = target - n
            if x in temp:
                return [temp[x],i]
            temp[n] = i
            