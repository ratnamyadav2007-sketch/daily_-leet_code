class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum = 0
        left_q = 0
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
                
        right_sum = 0
        right_q = 0
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
                
        diff_sum = left_sum - right_sum
        diff_q = left_q - right_q
        
        if diff_q % 2 != 0:
            return True
        
        return diff_sum + (diff_q // 2) * 9 != 0