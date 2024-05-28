class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        prevNot0Elem = 0
        res = 0

        for elem in bank:
            count = elem.count('1')
            if count != 0:
                res += prevNot0Elem * count
                prevNot0Elem = count
        
        return res



        
