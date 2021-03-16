package delete

import "testing"

func TestDeleteNode(t *testing.T) {
	var testCases = []struct {
		head []int
		node int
		want []int
	}{
		{[]int{4, 5, 1, 9}, 5, []int{4, 1, 9}},
		{[]int{4, 5, 1, 9}, 1, []int{4, 5, 9}},
		{[]int{1, 2, 3, 4}, 3, []int{1, 2, 4}},
		{[]int{0, 1}, 0, []int{1}},
		{[]int{-3, 5, -99}, -3, []int{5, -99}},
	}

	for _, tc := range testCases {
		if r := toSlice(delete)
	}
}


