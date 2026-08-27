from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        best_prefix_len = -1
        best_char = None
        
        current_counts = Counter(s)
        
        for i in range(n):
            target_char = target[i]
            
            for c_code in range(ord(target_char) + 1, ord('z') + 1):
                c = chr(c_code)
                if current_counts[c] > 0:
                    best_prefix_len = i
                    best_char = c
                    break
            
            if current_counts[target_char] > 0:
                current_counts[target_char] -= 1
            else:
                break
                
        if best_prefix_len == -1:
            return ""
        
        res_counts = Counter(s)
        result = list(target[:best_prefix_len])
        
        for ch in result:
            res_counts[ch] -= 1
            
        res_counts[best_char] -= 1
        result.append(best_char)
        
        for c_code in range(ord('a'), ord('z') + 1):
            c = chr(c_code)
            if res_counts[c] > 0:
                result.append(c * res_counts[c])
                
        return "".join(result)