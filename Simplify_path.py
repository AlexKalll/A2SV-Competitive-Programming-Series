class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur_ = ""

        for c in path + "/":
            if c == "/":
                if cur_ == "..":
                    if stack: 
                        stack.pop()
                elif cur_ != "" and cur_ != ".":
                    stack.append(cur_)
                cur_ = ""
            else:
                cur_ += c

        return "/" + "/".join(stack)
