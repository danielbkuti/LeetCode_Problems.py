def sortedSquares(self, nums):
    squaredList = []
    for i in nums:
        squaredList.append(i ** 2)

    squaredList.sort()
    return squaredList