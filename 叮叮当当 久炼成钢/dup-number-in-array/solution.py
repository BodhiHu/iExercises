from typing import List


class Solution:
    def findRepeatNumber(nums: List[int]) -> int:
        for i, v in enumerate(nums):
            print('index: %d, value: %d' % (i, v))
            # Solution 1:
            if (v in nums[i+1:]):
                print('found duplicate num: %1d' % v)
                return v
            #
            # Solution 2:
            # try:
            #     if (nums.index(v, i + 1) >= 0):
            #         print('found duplicate num: %1d' % v)
            #         return v
            # except Exception as exc:
            #     print('ERROR: ', exc)
            #     return -1


if (__name__ == '__main__'):
    Solution.findRepeatNumber([100, 2, 0, 2, 1, 3, 4, 5])
