class Solution:
    """
    Intuition:
        Split the array in half at every iteration until the
        target is found.

    Runtime:
        O(log n)... it's binary search dawg.

    Memory:
        O(1) since we only store pointers.
    """

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
