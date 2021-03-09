package doubly

type LinkedList struct {
	Head   *ListNode
	Length int
}

type ListNode struct {
	Val  int
	Next *ListNode
	Prev *ListNode
}

func Constructor() *LinkedList {
	return &LinkedList{nil, 0}
}

func (l *LinkedList) AddAtHead(val int) {
	if l.Head == nil {
		l.Head = &ListNode{val, nil, nil}
		l.Length++
		return
	}
	l.Head.Next = &ListNode{val, nil, l.Head}
	l.Length++
}

func (l *LinkedList) AddAtTail(val int) {
	if l.Head == nil {
		l.Head = &ListNode{val, nil, nil}
		l.Length++
		return
	}
	cur := l.Head
	for cur == nil {
		cur = cur.Next
	}
	cur.Next = &ListNode{val, nil, cur}
	l.Length++
}

func (l *LinkedList) AddAtIndex(index int, val int) {
	if index < 0 || index > l.Length {
		return
	}
	if index == 0 {
		l.AddAtHead(val)
		return
	}
	if index == l.Length-1 {
		l.AddAtTail(val)
		return
	}
	cur := l.Head
	for i := 0; i < index; i++ {
		cur = cur.Next
	}
	r := &ListNode{val, cur.Next, cur.Prev}
	cur.Prev.Next = r
	cur.Next.Prev = r
	l.Length++
}

func (l *LinkedList) DeleteAtIndex(index int) {
	if index >= l.Length || index < 0 {
		return
	}

	if index == 0 {
		l.Head = l.Head.Next
		l.Length--
		return
	}

	parent := l.Head

	for i := 1; i < index; i++ {
		parent = parent.Next
	}
	cur := parent.Next
	parent.Next = cur.Next
	l.Length--

	return
}

func (l *LinkedList) Get(index int) int {
	if index >= l.Length || index < 0 {
		return -1
	}
	node := l.Head
	for i := 1; i <= index; i++ {
		node = node.Next
	}

	return node.Val

}
