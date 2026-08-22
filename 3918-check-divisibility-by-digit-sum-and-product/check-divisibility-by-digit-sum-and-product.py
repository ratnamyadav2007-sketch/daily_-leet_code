class Solution:

  def checkDivisibility(self, n: int) -> bool:
    digits = [int(d) for d in str(n)]

    digit_sum = sum(digits)

    digit_prod = 1
    for d in digits:
      digit_prod *= d

    total_sum = digit_sum + digit_prod

    return n % total_sum == 0