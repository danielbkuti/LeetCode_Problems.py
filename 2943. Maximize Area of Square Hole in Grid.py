class Solution(object):

    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        hBars.sort()
        vBars.sort()
        hmax, vmax = 1, 1
        hcur, vcur = 1, 1
        for i in range(1, len(hBars)):
            if hBars[i] <= hBars[i-1] + 1:
                hcur += 1
            else:
                hcur = 1
            hmax = max(hmax, hcur)
        for i in range(1, len(vBars)):
            if vBars[i] <= vBars[i-1] + 1:
                vcur += 1
            else:
                vcur = 1
            vmax = max(vmax, vcur)

        maxSqr = (min(hmax, vmax)+1)
        return maxSqr * maxSqr


result = Solution()
print(result.maximizeSquareHoleArea(2, 3, [2, 4], [2]))

