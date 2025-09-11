class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Intuition:
            We can use a fixed sliding window and counters that keep track of the frequency of letters
            in the substring and the fixed window. At every increment of the window, we simply check
            if the counters match up.

        Runtime:
            O(n) -> n = length of s2. We need one pass over s2. Thus, linear time.

        Memory:
            O(1) -> Counter arrays are bounded by number of letters (26), simplifies to constant space.
        """

        if len(s2) < len(s1):
            return False

        counter1 = [0] * 26
        counter2 = [0] * 26
        for i in range(len(s1)):
            counter1[ord(s1[i]) - ord('a')] += 1
            counter2[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if counter1 == counter2:
                return True

            counter2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            counter2[ord(s2[i]) - ord('a')] += 1

        return counter1 == counter2
