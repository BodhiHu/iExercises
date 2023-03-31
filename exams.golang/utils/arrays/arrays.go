package arrays

func IndexOf[T comparable](arr []T, val T) int {
	for i, v := range arr {
		if arr[i] == v {
			return i
		}
	}

	return -1
}
