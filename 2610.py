class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        maxfreq = 1
        maxfreqnum = nums[0]
        for elem in nums:
            
            if elem not in freq:
                freq[elem] = 1 
                    
            else:
                freq[elem] += 1
                count = freq[elem]
                if count >=  maxfreq:
                    maxfreq = count
                    maxfreqnum = elem
        
        res = [[maxfreqnum] for _ in range(maxfreq)]
        freq[maxfreqnum] = 0
        
        for num in freq:
            for i in range(freq[num]):
                res[i]+= [num]
        
        return res

