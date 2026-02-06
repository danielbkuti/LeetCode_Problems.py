from ast import List


class Solution(object):
    def getEdges(self, fences: List[int], edge: int) -> set:
        grid = sorted([1] + fences + [edge])
        return {
            grid[j] - grid[i]
            for i in range(len(grid))
            for j in range(i+1, len(grid))
        }
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        hEdges = self.getEdges(hFences, m)
        vEdges = self.getEdges(vFences, n)
        max_edge = max(hEdges & vEdges, default=0)
        MOD = 10 ** 9 + 7

        return max_edge % MOD if max_edge else -1


result = Solution()
print(result.maximizeSquareArea(4, 3, [2, 3], [2]))
