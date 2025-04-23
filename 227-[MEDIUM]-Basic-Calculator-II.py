class Solution1:
    """
    Intuition:
        Use string parsing. We separate numbers from operators and store
        them in an array called components. Then, we perform the operations
        while maintaining priority.

        We perform a first pass with a stack over the elements and check
        for multiplication and division.

        After the first pass, we check if there are any other operations left
        to do.

        The second pass checks for addition and subtraction operations.

    Notes:
        Runtime (although linear) is TERRIBLE... we can definitely optimize
        parsing and usage of stack
    """

    def calculate(self, s: str) -> int:
        components = []
        ix = 0

        while ix < len(s):
            # Skip whitespaces
            if s[ix] == " ":
                ix += 1
            # Case number
            elif s[ix].isnumeric():
                jx = ix

                while ix < len(s) and s[ix].isnumeric():
                    ix += 1

                num = int(s[jx:ix])
                components.append(num)
            # Case operator
            else:
                components.append(s[ix])
                ix += 1

        stack = []
        kx = 0

        while kx < len(components):
            elmt = components[kx]

            if elmt == "*" or elmt == "/":
                num1, num2 = stack.pop(), components[kx + 1]
                res = num1 * num2 if elmt == "*" else num1 // num2
                stack.append(res)
                kx += 2
            else:
                stack.append(elmt)
                kx += 1

        if len(stack) == 1:
            return stack[0]

        components, stack = stack, []
        kx = 0

        while kx < len(components):
            elmt = components[kx]

            if elmt == "+" or elmt == "-":
                num1, num2 = stack.pop(), components[kx + 1]
                res = num1 + num2 if elmt == "+" else num1 - num2
                stack.append(res)
                kx += 2
            else:
                stack.append(elmt)
                kx += 1

        return stack[0]
