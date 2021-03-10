package doubly

type MyLinkedList struct {
	root   *MyListNode
	length int
}

type MyListNode struct {
	val  int
	next *MyListNode
	prev *MyListNode
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	return MyLinkedList{nil, 0}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	if index < 0 || index >= this.length {
		return -1
	}

	cur := this.root
	for i := 1; i <= index; i++ {
		cur = cur.next
	}

	return cur.val
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	if this.length == 0 {
		this.root = &MyListNode{val, nil, nil}
		this.length++
		return
	}

	n := &MyListNode{val, this.root, nil}
	this.root.prev = n
	this.root = n
	this.length++
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	if this.length == 0 {
		this.root = &MyListNode{val, nil, nil}
		this.length++
		return
	}

	cur := this.root
	for cur.next != nil {
		cur = cur.next
	}

	n := &MyListNode{val, nil, nil}
	cur.next = n
	n.prev = cur
	this.length++
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 || index > this.length {
		return
	}

	if index == 0 {
		this.AddAtHead(val)
		return
	}

	if index == this.length {
		this.AddAtTail(val)
		return
	}

	cur := this.root
	for i := 1; i <= index; i++ {
		cur = cur.next
	}

	n := &MyListNode{val, nil, nil}
	cur.prev.next = n
	n.prev = cur.prev
	cur.prev = n
	n.next = cur
	this.length++
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index >= this.length {
		return
	}

	if index == 0 {
		this.root = this.root.next
		this.length--
		return
	}

	cur := this.root
	for i := 1; i <= index; i++ {
		cur = cur.next
	}

	cur.prev.next = cur.next
	if cur.next != nil {
		cur.next.prev = cur.prev
	}
	this.length--
}
