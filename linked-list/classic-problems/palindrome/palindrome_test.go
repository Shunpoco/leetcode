package palindrome

import "testing"

func TestIsPlaindrome(t *testing.T) {
	var testCases = []struct {
		head []int
		want bool
	}{
		{[]int{1, 2, 2, 1}, true},
		{[]int{1, 2}, false},
		{[]int{1, 2, 1}, true},
		{[]int{1}, true},
		{[]int{8, 0, 7, 1, 7, 7, 9, 7, 5, 2, 9, 1, 7, 3, 7, 0, 6, 5, 1, 7, 7, 9, 3, 8, 1, 5, 7, 7, 8, 4, 0, 9, 3, 7, 3, 4, 5, 7, 4, 8, 8, 5, 8, 9, 8, 5, 8, 8, 4, 7, 5, 4, 3, 7, 3, 9, 0, 4, 8, 7, 7, 5, 1, 8, 3, 9, 7, 7, 1, 5, 6, 0, 7, 3, 7, 1, 9, 2, 5, 7, 9, 7, 7, 1, 7, 0, 8}, true},
	}

	for _, tc := range testCases {
		if r := isPalindrome(toListNode(tc.head)); r != tc.want {
			t.Errorf("isPalindrome(%v) = %t, expected %t", tc.head, r, tc.want)
		}
	}
}

func toListNode(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}

	r := &ListNode{nums[0], nil}
	c := r
	for i := 1; i < len(nums); i++ {
		n := &ListNode{nums[i], nil}
		c.Next = n
		c = c.Next
	}

	return r
}
