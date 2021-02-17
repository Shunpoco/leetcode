package minstack

type MinStack struct {
	values []component
	len    int
}

type component struct {
	val int
	min int
}

func Constructor() MinStack {
	return MinStack{[]component{}, 0}
}

func (this *MinStack) Push(x int) {
	comp := component{x, 0}
	if this.len == 0 {
		comp.min = x
	} else {
		topMin := this.values[this.len-1].min
		if topMin > x {
			comp.min = x
		} else {
			comp.min = topMin
		}
	}
	this.values = append(this.values, comp)
	this.len++
}

func (this *MinStack) Pop() {
	this.values = this.values[:this.len-1]
	this.len--
}

func (this *MinStack) Top() int {
	val := this.values[this.len-1]

	return val.val
}

func (this *MinStack) GetMin() int {
	return this.values[this.len-1].min
}
