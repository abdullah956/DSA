from cmath import inf


class Solution:
    def minDiffInBST(self, root) -> int:
        if not root:
            return
        stack = []
        current = root
        prev = None
        res = float(inf)
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if prev:
                    res = min(res, current.val - prev.val)
                prev = current
                current = current.right
        return res
