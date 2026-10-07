class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed), reverse=True)
        stack = []

        for position, speed in cars:
            time_to_arrival = (target - position) / speed
            if not stack or time_to_arrival > stack[-1]:
                stack.append(time_to_arrival)
            
        return len(stack)