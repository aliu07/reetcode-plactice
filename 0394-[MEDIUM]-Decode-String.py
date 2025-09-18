class Solution1:
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
            if s[ix] != "]":
                stack.append(s[ix])
            else:
                sequence = stack.pop()

                while stack and stack[-1] != "[":
                    sequence = stack.pop() + sequence

                # Pop '[' character
                stack.pop()

                multiplier = stack.pop()

                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                decoded = sequence * int(multiplier)

                stack.append(decoded)

            ix += 1

        return "".join(stack)


class Solution2:
    """
    Intuition:
        Instead of a singular stack, we can opt to use 2 distinct stacks. One holds
        all the multipliers while the other holds all the char sequences.

        Case 1) If the current character is a digit (0-9), append it to currMul.

        Case 2) If the current character is a letter (a-z), append it to currSeq.

        Case 3) If current character is a opening bracket [, push currMul and currSeq
                onto their respective stacks.

        Case 4) Closing bracket ]: We must begin the decoding process,

                We must decode the currSeq. Pop the multiplier from its stack and decode
                the pattern multiplier[currSeq]

                As the sequences stack contains a possible previously decoded string, pop
                that sequence from the sequences stack.
                Update the decodedString = decodedString + multiplier[currSeq]

    Runtime:
        O(maxK * n) since each substring is built once and then repeated 'k' times
        unliked the single-stack approach which may re-decode the same substring
        multiple times due to nesting.

    Memory:
        O(m + n) where n is the number of a-z chars in the input string and m is
        the number of digit chars in the input string.
    """

    def decodeString(self, s: str) -> str:
        sequences = []
        multipliers = []

        currSeq = ""
        currMul = ""

        for char in s:
            if char.isdigit():
                currMul += char
            elif char == "[":
                multipliers.append(int(currMul))
                sequences.append(currSeq)

                # Reset values
                currSeq, currMul = "", ""
            elif char == "]":
                decoded = sequences.pop()
                multiplier = multipliers.pop()

                decoded = decoded + currSeq * multiplier

                currSeq = decoded
            else:
                currSeq += char

        return currSeq
