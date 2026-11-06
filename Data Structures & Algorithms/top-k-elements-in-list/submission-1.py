class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = []
        nums.sort()
        count = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count = count + 1
                if (count == k) or (count > k):
                    temp.append(nums[i])
            else:
                count = 1
        return list(set(temp))


