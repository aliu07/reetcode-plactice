from typing import List


class Solution:
    """
    Intuition:
        We use DFS to backtrack. We iterate through our board to find
        potential starting points. Once one if found, we can DFS to
        explore and branh out until we either find the word or we've
        exhausted all possibilities.

    Runtime:
        Let m, n be the dimensions of the board.

        Let k be the length of the word.

        In the worst case, each cell of the board is a potential starting
        point which would take O(m * n) time.

        For each starting point, we iterate recursively. At each step, we
        have 4 possible choices, leadin to an additional O(4^k) factor.

        Overall, we have O(m * n * 4^k).

        Note: In reality, only the first cell will have 4 valid choices.
              Subsequent cells can only pick 3 since the one it from the
              previous call now holds a '#' placeholder. Thus, the true
              tight upper bound is O(m * n * 3^(k - 1)).

    Memory:
        Let k be the length of word.

        Recursive call stack takes at most O(k). Overall O(k) memory.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])

        def dfs(r, c, ix):
            if ix == len(word):
                return True

            if r < 0 or c < 0 or r >= M or c >= N or board[r][c] != word[ix]:
                return False

            board[r][c] = "#"
            res = (
                dfs(r - 1, c, ix + 1)
                or dfs(r + 1, c, ix + 1)
                or dfs(r, c - 1, ix + 1)
                or dfs(r, c + 1, ix + 1)
            )
            board[r][c] = word[ix]
            return res

        for r in range(M):
            for c in range(N):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
