class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        res = 0

        while left <= right:
            mid = (left + right) // 2
            coins_needed = (mid * (mid + 1)) // 2

            if coins_needed == n:
                return mid
            elif coins_needed < n:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res