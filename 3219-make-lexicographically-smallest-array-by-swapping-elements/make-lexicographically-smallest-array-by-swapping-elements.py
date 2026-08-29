class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * n
        
        groups = []
        curr_group = [sorted_nums[0]]
        
        for i in range(1, n):
            if sorted_nums[i][0] - sorted_nums[i - 1][0] <= limit:
                curr_group.append(sorted_nums[i])
            else:
                groups.append(curr_group)
                curr_group = [sorted_nums[i]]
        groups.append(curr_group)
        
        
        for group in groups:
            
            indices = sorted(idx for val, idx in group)
            
            for i, (val, _) in enumerate(group):
                result[indices[i]] = val
                
        return result