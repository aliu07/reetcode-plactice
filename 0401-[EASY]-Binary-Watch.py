from typing import List


class Solution:
    """
    Intuition:
        We can reason about the combinations of LED lights as a binary
        string. A given bit is 1 if it is turned on and 0 if not. Our
        task is to choose all unique combinations of such binary strings.

        To do this, we can use a backtracking approach. Our base case is
        when we have no more remaining LEDs to select. Our recursive step
        only explores combinations that have not been explored yet (hence
        why the startIx arg is needed). At each recursive step, we only
        continue exploring if the new hour and minute are valid.

    Runtime:
        We are choosing turnedOn LEDs out of 10 possible LEDs which is
        10 choose turnedOn. The worst case is when turnedOn = 5, which
        yields O(252) ~ O(1).

    Memory:
        Our memory complexity is represented by the maximum depth of our
        recursion tree i.e. the number of decisions to be made. In our
        case, this is O(turnedOn). Since the max value of turnedOn is 10,
        our memory complexity can be simplified to O(1).
    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # think of each combination of LEDs as a bit string of length 10
        # indices 0-3 for hrs, 4-9 for mins
        bitMap = {
            0: 1,
            1: 2,
            2: 4,
            3: 8,
            4: 1,
            5: 2,
            6: 4,
            7: 8,
            8: 16,
            9: 32,
        }
        res = []

        def backtrack(startIx, rem, hr, min):
            if rem == 0:
                time = str(hr) + ":"
                if min < 10:
                    time += "0"
                time += str(min)
                res.append(time)
                return

            for ix in range(startIx, 10):
                nxtHr, nxtMin = hr, min

                if ix < 4:  # hrs
                    nxtHr |= bitMap[ix]
                else:  # mins
                    nxtMin |= bitMap[ix]

                if nxtHr <= 11 and nxtMin <= 59:
                    backtrack(ix + 1, rem - 1, nxtHr, nxtMin)

        backtrack(0, turnedOn, 0, 0)
        return res
