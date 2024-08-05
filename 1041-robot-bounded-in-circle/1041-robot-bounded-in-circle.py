class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # N0 E1 S2 W3
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        x, y = 0, 0
        
        for instruction in instructions:
            if instruction == 'G':
                dx, dy = directions[direction]
                x, y = x + dx, y + dy
            elif instruction == 'L':
                direction = (direction - 1) % 4
            else: 
                direction = (direction + 1) % 4
        
        return (x == 0 and y == 0) or direction != 0