from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            print(cost[i])

        print(cost[0], cost[1])
        return min(cost[0], cost[1])


s = Solution()
print(s.minCostClimbingStairs([5, 10, 15, 20]))
