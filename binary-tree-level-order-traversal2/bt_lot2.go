package bt

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	list := depthFirstSearch(root, 0, [][]int{})
	var result = [][]int{}
	for idx := range list {
		result = append(result, list[len(list)-1-idx])
	}
	return result
}

func depthFirstSearch(root *TreeNode, depth int, list [][]int) [][]int {
	if root == nil {
		return list
	}
	if len(list) <= depth {
		list = append(list, []int{root.Val})
	} else {
		list[depth] = append(list[depth], root.Val)
	}
	list = depthFirstSearch(root.Left, depth+1, list)
	list = depthFirstSearch(root.Right, depth+1, list)

	return list
}
