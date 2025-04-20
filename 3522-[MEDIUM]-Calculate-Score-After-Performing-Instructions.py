from typing import List

class Solution:
    """
    Intuition:
        Just keep track of visited indices with a hashset.
    """

    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        if not instructions:
            return 0

        # Keep track of seen instruction indices
        seen = set()
        # Starting index
        ix = 0
        # Count score
        score = 0

        while 0 <= ix < len(instructions) and ix not in seen:
            seen.add(ix)

            # Add to score
            if instructions[ix] == "add":
                score += values[ix]
                ix += 1
            # Jump
            else:
                ix += values[ix]

        return score
