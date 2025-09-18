from typing import List


class Solution:
    """
    Intuition:
        The key modulo property here is this: (a * b) mod n = ((a mod n) * (b mod n)) mod n

        We use a bottom-up DP approach. The idea that hints towards a DP approach is that at
        each number, we can either decide to start a contiguous subarray at the current position
        or extend an existing one.

    Runtime: O(n * k)

    Memory: O(n)
    """

    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        # Let dp[i] = count of ways to achieve remainder of i when dividing by k
        dp = [0] * k

        for num in nums:
            newTab = [0] * k

            # Extend an existing subarray
            for mod in range(k):
                if dp[mod] > 0:
                    newMod = (mod * num) % k
                    newTab[newMod] += dp[mod]

            # Start a subarray
            newTab[num % k] += 1

            # Increment results
            for mod in range(k):
                res[mod] += newTab[mod]

            dp = newTab

        return res
