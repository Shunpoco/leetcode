package main

import "testing"

type test struct {
	nums  []int
	ideal []string
}

func TestSummaryRanges(t *testing.T) {
	tests := []test{
		{
			[]int{0, 1, 2, 4, 5, 7},
			[]string{"0->2", "4->5", "7"},
		},
		{
			[]int{0, 2, 3, 4, 6, 8, 9},
			[]string{"0", "2->4", "6", "8->9"},
		},
		{
			[]int{},
			[]string{},
		},
	}

	for i, test := range tests {
		actual := summaryRanges(test.nums)

		if len(actual) != len(test.ideal) {
			t.Errorf("Length does not match\n")
			continue
		}
		for j := 0; j < len(actual); j++ {
			if actual[j] != test.ideal[j] {
				t.Errorf("Value does not match: %d", i)
			}
		}
	}
}
