class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        x = []
        for i in nums:
            if i in temp:
                temp[i] = temp[i]+1
                if temp[i] >= k and i not in x:
                    x.append(i)
            temp[i] = 1
        return x
        