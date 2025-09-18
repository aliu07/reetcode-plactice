from collections import deque


class Solution1:
    """
    Intuition:
        Use built-in functions. Simplest solution. Some interviewers
        might not like this type of solution. See alternative solution
        below for more 'algorithmic' approach.

    Runtime: O(n)

    Memory: O(n)
    """

    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        # Filter out empty strings
        words = [word for word in words if word]
        return " ".join(words[::-1])


class Solution2:
    """
    Intuition:
        Use pointers and a queue to process the words. We use pointers
        to isolate each word token. We append to the head of the array
        at each step to get the reverse order of the words.

    Runtime: O(n)

    Memory: O(n)
    """

    def reverseWords(self, s: str) -> str:
        q = deque()
        ix = 0

        while ix < len(s):
            if s[ix] != " ":
                # Save left boundary
                l = ix

                while ix < len(s) and s[ix] != " ":
                    ix += 1

                # Appendleft to reverse order
                q.appendleft(s[l:ix])

            ix += 1

        return " ".join(q)
