class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = list(s)

        for i in t:
            if i in temp:
                temp.remove(i)
            else:
                return False
        return True