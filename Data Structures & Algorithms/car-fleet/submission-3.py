class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        arr = sorted(zip(position, speed), reverse = True)
        cnt = 0
        stack = []
        for p,s in arr:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)
        

        