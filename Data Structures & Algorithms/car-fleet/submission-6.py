class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed),reverse=True)
        stack = []

        for p,s in cars:
            tta = (target - p) / s
            if not stack or tta > stack[-1]:
                stack.append(tta)
        
        return len(stack)