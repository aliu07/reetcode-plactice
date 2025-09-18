class Solution1:
    """
    Intuition:
        We maintain a stack to be able to pop components in the
        filepath whenever we encounter '..'.

    Notes:
        - Can leverage built-in functions in python to do string
        splitting
    """

    def simplifyPath(self, path: str) -> str:
        stack = []
        ix = 0

        while ix < len(path):
            # Skip consecutive slashes
            while ix < len(path) and path[ix] == "/":
                ix += 1

            name = ""

            # Get directory/file name
            while ix < len(path) and path[ix] != "/":
                name += path[ix]
                ix += 1

            # Treat special cases
            if name == "." or name == "":
                continue
            elif name == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(name)

        return "/" + "/".join(stack)


class Solution2:
    """
    Improvements:
        - Use built-in functions to improve runtime performance
    """

    def simplifyPath(self, path: str) -> str:
        stack = []

        for s in path.split("/"):
            if s == "" or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)

        return "/" + "/".join(stack)
