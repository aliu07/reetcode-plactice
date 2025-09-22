class TimeMap:
    """
    Intuition:
        We build a dictionary and hash by key. For each key, store an array of
        tuples that map the timestamp and its respective value.

        A brute force approach would be to scan all the possible timestamps
        within the array which would take linear time.

        We know for a fact that a tuple with a later timestanp could not have
        been appended before one with an earlier timestamp. In other words,
        our tuples are appended in chronological order i.e. sorted. Using this
        fact, we can leverage binary search to reduce the runtime to log-scale
        instead.

    Runtime:
        Calling set() takes O(1) time.

        Calling get() takes O(log m) time where m is the number of timestamps.

    Memory:
        For n keys and m timestamps, our dictionary `tmap` would be bounded
        by O(n * m).
    """

    def __init__(self):
        # {key: [(timestamp, value)]}
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.tmap[key]
        l, r = 0, len(self.tmap[key]) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
