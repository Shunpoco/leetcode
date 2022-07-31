package main

type NumArray struct {
    nums []int
    sums []int
}


func Constructor(nums []int) NumArray {
    sums := make([]int, len(nums)+1)
    sum := 0
    for i, v := range nums {
        sum += v
        sums[i+1] = sum
    }
    
    return NumArray{
        nums,
        sums,
    }
}


func (this *NumArray) Update(index int, val int)  {
    diff := val - this.nums[index]
    this.nums[index] = val
    
    for i := index+1; i < len(this.sums); i++ {
        this.sums[i] += diff
    }
}


func (this *NumArray) SumRange(left int, right int) int {
    return this.sums[right+1] - this.sums[left]
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
