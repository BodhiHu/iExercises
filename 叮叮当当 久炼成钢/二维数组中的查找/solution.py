from random import randint
from typing import List


class Solution:
    def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
        for i, arr in enumerate(matrix):
            if (target in arr):
                print(True, target, 'is in: ')
                return True

        print(False, target, 'is not in: ')
        return False


if (__name__ == '__main__'):
    Solution.findNumberIn2DArray(
      [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
      ],
      randint(0, 80)
    )
