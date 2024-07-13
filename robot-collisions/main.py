class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [[pos, health, direct, ori] for pos, health, direct, ori in zip(positions, healths, directions, [i for i in range(len(positions))])]
        robots.sort()

        stack = []

        for robot in robots:
            while robot[1] > 0 and len(stack) > 0 and stack[-1][2] == 'R' and robot[2] == 'L':
                if stack[-1][1] > robot[1]:
                    robot[1] = 0
                    stack[-1][1] -= 1
                elif stack[-1][1] == robot[1]:
                    robot[1] = 0
                    stack.pop(-1)
                else:
                    robot[1] -= 1
                    stack.pop(-1)

            if robot[1] > 0:
                stack.append(robot)

        r = [(robot[3], robot[1]) for robot in stack]
        r.sort()
        result = [robot[1] for robot in r]

        return result
