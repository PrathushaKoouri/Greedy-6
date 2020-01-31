class Solution:
    '''
    Accepeted on leetcode(991)
    Time - O(N), minimum no. of steps
    space - O(1)
    Approach: Greedy approach(reverse backtrack)
    1. start from Y when Y is greater than X until X == Y
    2. increase the cost each time we do one operation(reverse from what given, bottom up approach) among 2.
    3. At the end return cost + X -Y, just to handle X > Y edge case.

    '''

    def brokenCalc(self, X: int, Y: int) -> int:
        cost = 0
        while X < Y:
            if Y % 2 == 0:  # even
                Y = Y / 2
            else:
                Y = Y + 1
            cost += 1
        return int(cost + X - Y)