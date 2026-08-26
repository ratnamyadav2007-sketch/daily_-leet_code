class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, char in enumerate(s) if char == '1']
        
        if len(ones) < k:
            return ""
        
        ans = ""
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                ans = sub
                
        return ans