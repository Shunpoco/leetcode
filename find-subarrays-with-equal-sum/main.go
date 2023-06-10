package main

func findSubarrays(nums []int) bool {
	mem := make(map[int]bool)

	n := len(nums)
	for i := 0; i < n-1; i++ {
		v := nums[i+1] + nums[i]
		if mem[v] {
			return true
		}
		mem[v] = true
	}

	return false
}
