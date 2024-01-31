package smallest_k_numbers

func SmallestKNums(nums *[]int, k int) []int {
	return (*QuickSort(nums))[0:k]
}

func QuickSort(nums *[]int) *[]int {
	if len(*nums) <= 1 {
		return nums
	}

	base := (*nums)[0]
	leftArr := []int{}
	rightArr := []int{}

	for _, v := range (*nums)[1:] {
		if v <= base {
			leftArr = append(leftArr, v)
		} else {
			rightArr = append(rightArr, v)
		}
	}

	sortedArr := []int{}
	sortedArr = append(append((append(sortedArr, leftArr...)), base), rightArr...)

	return &sortedArr
}
