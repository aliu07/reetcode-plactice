class Solution:
    """
    Intuition:
        We use 2 pointers to traverse each string respectively. The problem essentially
        outline 4 cases...
        1 - If chars at both ix & jx are a-z chars, we just compare
        2 - If we hit a 0 in abbr, then we return False since it violates the specified
            rules
        3 - If we hit a numerical digit in abbr, we need to parse the number and increment
            ix appropriately
        4 - If we hit this case, it means that the chars at ix and jx do not match up, so
            return False.

    Notes:
        The only valid end state is where ix == len(word) and jx == len(abbr), meaning we
        have traversed the entirety of boths strings.

        If either index violate the condition, then we know the abbreviation is invalid.
    """

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ix, jx = 0, 0

        while ix < len(word) and jx < len(abbr):
            if word[ix] == abbr[jx]:
                ix += 1
                jx += 1
            elif abbr[jx] == '0':
                return False
            elif abbr[jx].isnumeric():
                # Store starting index of numeric substring
                kx = jx

                while jx < len(abbr) and abbr[jx].isnumeric():
                    jx += 1

                ix += int(abbr[kx: jx])
            else:
                return False

        return ix == len(word) and jx == len(abbr)
