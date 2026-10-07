class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_ = "{[("
        close = "]})"
        for char in s:
            print(stack)
            if char in open_:
                stack.append(char)
            if stack:
                if char in close:
                    if char == "]" and stack[-1] == "[":
                        stack.pop()
                    elif char == ")" and stack[-1] == "(":
                        stack.pop()
                    elif char == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
            else:
                return False
        return not stack
