from typing import List


class Codec:
    """
    Intuition:
        We can use a delimiter and the lengths of each string (since they vary) to do the encoding. We build
        the encoded string by processing each string in the following structure: <length><delimiter><string>.
        This way, we can parse the prefix length until we hit the delimiter and then fetch the string content
        via the length property.

        To decode, we can leverage two pointers to parse each chunk of the encoded string (length prefix and
        then string content).

    Runtime:
        O(m) for encode and decode -> m is the sum of the lengths of each string

    Memory:
        O(m) for encode -> need to store res string
        O(m) for decode -> storing strings into res array
    """

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""

        ix = 0
        res = []

        while ix < len(s):
            jx = ix

            while s[jx] != "#":
                jx += 1

            length = int(s[ix:jx])
            ix = jx + 1
            jx = ix + length
            res.append(s[ix:jx])
            ix = jx

        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
