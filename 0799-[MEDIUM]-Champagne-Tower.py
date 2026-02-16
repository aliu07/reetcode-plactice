class Solution:
    """
    Intuition:
        We take a DP approach. The result of the current row of glasses only depends
        on the previous row. Thus, we start at the first row and iterate until we hit
        the row we want to query on.

        We can split the glass filling logic into 2 sub-cases:
            - the glass is on the edge of the champagne tower (first & last glasses)
            - the glass is somewhere in the middle

        For the edge glasses, they only get filled by a single parent glass. For all
        the other middle glasses, we need to check 2 parent glasses.

    Runtime:
        Let query_row be N.

        We need O(N) iterations to exit the loop. At each iteration of the loop, we
        need up to O(100) ~ O(1) to init the next row array. We also need up to O(100)
        ~ O(1) to fill each glass of the next row.

        Overall, our runtime is O(N * 100) ~ O(N).

    Memory:
        O(100) in the worst case i.e. O(1).
    """

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        currRow = [poured]

        for _ in range(query_row):
            N = len(currRow)
            nextRow = [0] * (N + 1)

            # first
            nextRow[0] = max(0, (currRow[0] - 1) / 2)

            for i in range(1, N):
                nextRow[i] += max(0, (currRow[i - 1] - 1) / 2)
                nextRow[i] += max(0, (currRow[i] - 1) / 2)

            # last
            nextRow[-1] = max(0, (currRow[-1] - 1) / 2)

            currRow = nextRow

        return min(1, currRow[query_glass])
