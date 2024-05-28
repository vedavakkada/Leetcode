#first solution

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        saved = [0] * (n + 1)
        for i in range(n + 1):
            for elem in nums:
                if elem >= i:
                    saved[i] += 1
        
        for i in range(n + 1):
            if saved[i] == i:
                return i
        return -1

  #second solution
