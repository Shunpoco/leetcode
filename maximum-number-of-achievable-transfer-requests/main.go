package main

func maximumRequests(n int, requests [][]int) int {
	indegrees := make([]int, n)

	r := &R{0}

	r.exec(0, n, requests, indegrees, 0)

	return r.result
}

type R struct {
	result int
}

func (r *R) exec(start, n int, requests [][]int, indegrees []int, count int) {
	if start == len(requests) {
		for i := 0; i < n; i++ {
			if indegrees[i] != 0 {
				return
			}
		}
		r.result = max([]int{count, r.result})
		return
	}

	indegrees[requests[start][0]] -= 1
	indegrees[requests[start][1]] += 1
	r.exec(start+1, n, requests, indegrees, count+1)

	indegrees[requests[start][0]] += 1
	indegrees[requests[start][1]] -= 1
	r.exec(start+1, n, requests, indegrees, count)
}

func max(nums []int) int {
	var r = nums[0]
	for _, num := range nums {
		if r < num {
			r = num
		}
	}

	return r
}
