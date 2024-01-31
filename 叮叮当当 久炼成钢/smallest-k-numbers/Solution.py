from typing import *

class Solution:
    def __init__(self) -> None:
        pass

    def getSmallestKNumbers(self, arr: List[int], k: int) -> List[int]:
        return self.sort(arr)[0:k]

    def sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        base = arr[0]
        arr = arr[1:]
        leftArr = []
        rightArr = []
        for v in arr:
            if v <= base:
                leftArr.append(v)
            else:
                rightArr.append(v)

        print("Before sort recursion:", leftArr, rightArr)
        leftArr = self.sort(leftArr)
        rightArr = self.sort(rightArr)
        print("After sort recursion:", leftArr, rightArr)

        return leftArr + [base] + rightArr

