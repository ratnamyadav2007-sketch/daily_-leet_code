from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))
        
        arr.sort(key=lambda x: x[0])
        starts = [x[0] for x in arr]

        next_pos = []
        for i in range(n):
            r = arr[i][1]
            idx = bisect.bisect_right(starts, r)
            next_pos.append(idx)

        memo = {}

        def get_max(i: int, k: int):
            if k == 0 or i == n:
                return (0, [])
            if (i, k) in memo:
                return memo[(i, k)]

            skip_w, skip_path = get_max(i + 1, k)

            nxt = next_pos[i]
            take_w, take_path = get_max(nxt, k - 1)
            take_w += arr[i][2]
            
            take_path = sorted([arr[i][3]] + take_path)

            if take_w > skip_w:
                res = (take_w, take_path)
            elif skip_w > take_w:
                res = (skip_w, skip_path)
            else:
                res = (take_w, min(take_path, skip_path))

            memo[(i, k)] = res
            return res

        return get_max(0, 4)[1]