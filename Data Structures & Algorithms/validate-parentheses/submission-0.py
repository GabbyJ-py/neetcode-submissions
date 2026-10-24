class Solution:
    def isValid(self, s: str) -> bool:
        diction = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for i in s:
            if i in diction:
                if not stack:
                    return False
                if stack[-1] != diction[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
            

        return True if not stack else False
