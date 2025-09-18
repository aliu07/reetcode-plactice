from typing import List


class Solution:
    """
    Intuition:
        The problem is inherently DP. At each step, we can decide to either take the
        next element to include in our subarray or end the subarray at the current
        element.

        Since we are only worried with removing suffixes, we can just track a cumulative
        product variable and check if that cumulative product's remainder modulo k is
        equal to x.

    Notes:
        Had initially tried incorporating the solution to problem 3524 as a helper function,
        but the fact that we do not need to worry about removing a contiguous prefix simplifies
        the problem a lot.
    """

    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        res = []

        for ix, val, start, x in queries:
            nums[ix] = val

            # Count the number of subarrays starting at start index provided in query
            count = 0
            # To track product of subarray
            prod = 1

            for i in range(start, len(nums)):
                # Can save compute by breaking early since anything multiplied by 0 is 0
                if prod == 0:
                    # Need to update count if every x value in query is 0
                    if x == 0:
                        count += len(nums) - i

                    break

                prod = (prod * nums[i]) % k

                if prod == x:
                    count += 1

            res.append(count)

        return res
