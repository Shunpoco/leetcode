package minstack

import (
	"testing"
)

func TestMinStack(t *testing.T) {
	obj := Constructor()

	obj.Push(-2)
	obj.Push(0)
	obj.Push(-3)
	min := obj.GetMin()
	if min != -3 {
		t.Errorf("min must be equal -3, but %d", min)
	}
	obj.Pop()
	val := obj.Top()
	if val != 0 {
		t.Errorf("err")
	}
	min = obj.GetMin()
	if min != -2 {
		t.Errorf("min must be equal -2, but %d", min)
	}
}
