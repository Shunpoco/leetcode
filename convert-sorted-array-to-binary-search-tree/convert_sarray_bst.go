package convert

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	return build(0, len(nums), &nums)
}

func build(left, right int, nums *[]int) *TreeNode {
	if left == right {
		return nil
	}

	m := (left + right) / 2

	root := &TreeNode{(*nums)[m], nil, nil}
	root.Left = build(left, m, nums)
	root.Right = build(m+1, right, nums)

	return root
}
