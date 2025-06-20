from typing import List

class Solution:
    """
    Intuition:
        We can reduce the problem to a 2Sum problem by fixing the first element
        of the triplet to a set value.

        By sorting the array, we can be 'smart'
        about it. We essentially know if we hit a number greater than 0 that
        there are no more possible combinations since each subsequent element
        will be greater.

        Then, we iterate through this array and use a 2 pointer approach to solve
        for 2Sum to find the 2 remaining elements to form a valid triplet.

        To prevent duplicates, we need to introduce some logic to skip them.

    Runtime:
        O(n^2)

    Memory:
        O(n) to store result. O(1) auxiliary memory.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # Cannot form more triplets whose sum is 0
            if nums[i] > 0:
                break

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use 2 ptr approach on sorted partition
            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                # Found a valid triplet
                if currSum == 0:
                    x, y, z = nums[i], nums[l], nums[r]
                    res.append([x, y, z])

                    # Skip dupes
                    while l < len(nums) and nums[l] == y:
                        l += 1

                    # Skip dupes
                    while r >= 0 and nums[r] == z:
                        r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1

        return res
