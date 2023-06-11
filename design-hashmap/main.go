package main

type MyHashMap struct {
	size   int
	memory [][][]int
}

func Constructor() MyHashMap {
	size := 1000
	memory := make([][][]int, size)

	return MyHashMap{size, memory}
}

func (this *MyHashMap) hash(key int) int {
	return key % this.size
}

func (this *MyHashMap) search(key int) int {
	hash := this.hash(key)

	for i, node := range this.memory[hash] {
		if node[0] == key {
			return i
		}
	}

	return -1
}

func (this *MyHashMap) Put(key int, value int) {
	hash := this.hash(key)

	isC := this.search(key)
	if isC == -1 {
		this.memory[hash] = append(this.memory[hash], []int{key, value})
	} else {
		this.memory[hash][isC][1] = value
	}
}

func (this *MyHashMap) Get(key int) int {
	hash := this.hash(key)

	isC := this.search(key)

	if isC == -1 {
		return -1
	} else {
		return this.memory[hash][isC][1]
	}
}

func (this *MyHashMap) Remove(key int) {
	hash := this.hash(key)

	if idx := this.search(key); idx >= 0 {
		t := this.memory[hash][idx+1:]
		this.memory[hash] = this.memory[hash][:idx]
		this.memory[hash] = append(this.memory[hash], t...)
	}
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
