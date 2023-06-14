package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getMinimumDifference(root *TreeNode) int {
	_, _, result := exec(root)

	return result
}

func exec(node *TreeNode) (int, int, int) {
	if node == nil {
		return -1, -1, -1
	}

	ll, lr, lv := exec(node.Left)
	rl, rr, rv := exec(node.Right)

	l, r, v := node.Val, node.Val, -1

	if ll != -1 && l > ll {
		l = ll
	}
	if lr != -1 && r < lr {
		r = lr
	}
	if rl != -1 && l > rl {
		l = rl
	}
	if rr != -1 && r < rr {
		r = rr
	}

	if lr != -1 && (v == -1 || node.Val-lr < v) {
		v = node.Val - lr
	}

	if rl != -1 && (v == -1 || rl-node.Val < v) {
		v = rl - node.Val
	}

	if lv != -1 && v > lv {
		v = lv
	}
	if rv != -1 && v > rv {
		v = rv
	}

	return l, r, v
}
