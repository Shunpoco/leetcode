package main

type MyHashSet struct {
	size   int
	memory [][]int
}

func Constructor() MyHashSet {
	size := 1000
	memory := make([][]int, size)

	return MyHashSet{size, memory}
}

func (this *MyHashSet) Add(key int) {
	hash := key % this.size

	if search(this.memory[hash], key) == -1 {
		this.memory[hash] = append(this.memory[hash], key)
	}
}

func (this *MyHashSet) Remove(key int) {
	hash := key % this.size

	if idx := search(this.memory[hash], key); idx >= 0 {
		t := this.memory[hash][idx+1:]
		this.memory[hash] = this.memory[hash][:idx]
		this.memory[hash] = append(this.memory[hash], t...)
	}
}

func (this *MyHashSet) Contains(key int) bool {
	hash := key % this.size

	if idx := search(this.memory[hash], key); idx >= 0 {
		return true
	}
	return false
}

func search(arr []int, target int) int {
	for i, v := range arr {
		if v == target {
			return i
		}
	}

	return -1
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
