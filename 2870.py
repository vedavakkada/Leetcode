class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for elem in nums:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem] += 1
    
        steps = 0
        for elem in freq:
            n = freq[elem] 
            if n == 1:
                return -1
            steps += n//3
            if (n % 3 > 0):
                steps += 1

        return steps
            
        
