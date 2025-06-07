class Solution:
    """
    Intuition:
        The main pattern we need to observe is that we only ever need to decode
        when we hit a ']' character. For every other character, we just push onto
        the stack.

        When we do hit a closing bracket, we need to backtrack by popping elements
        from the stack to form the sequence of chars to be multiplied as well as
        the multiplier. We then push the decoded result back onto the stack.

    Runtime:
        O(maxK ^ countK * n) where n is the length of the input string 's', maxK is
        the greatest multiplier in the encoded string, and countK is the count of nested
        k values.

        There is a factor of maxK ^ countK to account for building decoded sequences.
        We need to multiply the sequence maxK times. In the worst case, we also have
        countK nested maxK multiplied sequences which causes the factor of maxK ^ countK.

    Memory:
        O(maxK ^ countK * n). The additional factor is explained in the runtime section.
        The decoded string in the stack has a length of this scale.
    """

    def decodeString(self, s: str) -> str:
        ix = 0
        stack = []

        while ix < len(s):
            if s[ix] != ']':
                stack.append(s[ix])
            else:
                sequence = stack.pop()

                while stack and stack[-1] != '[':
                    sequence = stack.pop() + sequence

                # Pop '[' character
                stack.pop()

                multiplier = stack.pop()

                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                decoded = sequence * int(multiplier)

                stack.append(decoded)

            ix += 1

        return ''.join(stack)
