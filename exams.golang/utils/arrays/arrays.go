package arrays

func IndexOf[T comparable](arr []T, val T) int {
	for i := 0; i < len(arr); i++ {
		if arr[i] == val {
			return i
		}
	}

	return -1
}
