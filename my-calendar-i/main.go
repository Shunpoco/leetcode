package main

type Node struct {
    start int
    end int
    next *Node
}

type MyCalendar struct {
    root *Node
}


func Constructor() MyCalendar {
    root := Node{-1, 0, nil}
    
    return MyCalendar{&root}
}


func (this *MyCalendar) Book(start int, end int) bool {
    cur := this.root
    prev := this.root
    for {
        if cur == nil || cur.start >= end {
            node := Node{start, end, cur}
            prev.next = &node
            break
        } else if cur.end <= start {
            prev = cur
            cur = cur.next
        } else {
            return false
        }
    }
    
    
    return true
}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
