package linkedlist

import "fmt"

type MyLinkedList struct {
	root   *node
	length int
}

type node struct {
	val  int
	next *node
}

// Constructor initializes the MyLinkedList object.
func Constructor() MyLinkedList {
	return MyLinkedList{nil, 0}
}

// Get the value of the index-th node in the linked list. if the index is invalid, return -1.
func (this *MyLinkedList) Get(index int) int {
	fmt.Println("Get", this.length)
	if index >= this.length || index < 0 {
		return -1
	}
	node := this.root
	for i := 1; i <= index; i++ {
		node = node.next
	}

	return node.val
}

// Add a node of value `val` before the first element of the linked list.
func (this *MyLinkedList) AddAtHead(val int) {
	fmt.Println("AddAtHead", this.length)
	n := &node{val, this.root}
	this.root = n
	this.length++
	return
}

// Add a node of value `val` as the last element of the linked list.
func (this *MyLinkedList) AddAtTail(val int) {
	fmt.Println("AddAtTail", this.length)
	n := &node{val, nil}
	if this.length == 0 {
		this.root = n
		this.length++
		return
	}
	parent := this.root
	for i := 1; i < this.length; i++ {
		parent = parent.next
	}
	parent.next = n
	this.length++
	return
}

// Add a node of value `val` before the index-th node in the linke list.
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	fmt.Println("AddAtIndex", this.length)
	if index > this.length || index < 0 {
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
	parent := this.root
	for i := 1; i < index; i++ {
		parent = parent.next
	}
	n := &node{val, parent.next}
	parent.next = n
	this.length++
	return
}

// Delete the index-th node in the liked list, if the index is valid.
func (this *MyLinkedList) DeleteAtIndex(index int) {
	fmt.Println("DeleteAtIndex", this.length)
	if index >= this.length || index < 0 {
		return
	}

	if index == 0 {
		this.root = this.root.next
		this.length--
		return
	}

	parent := this.root

	for i := 1; i < index; i++ {
		parent = parent.next
	}
	cur := parent.next
	parent.next = cur.next
	this.length--

	return
}
