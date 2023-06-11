package main

type SnapshotArray struct {
	id     int
	memory [][][]int
	buffer map[int]int
	length int
}

func Constructor(length int) SnapshotArray {
	memory := make([][][]int, length)
	buffer := make(map[int]int)

	return SnapshotArray{0, memory, buffer, length}
}

func (this *SnapshotArray) Set(index int, val int) {
	this.buffer[index] = val
}

func (this *SnapshotArray) Snap() int {
	for index, val := range this.buffer {
		this.memory[index] = append(this.memory[index], []int{val, this.id})
		delete(this.buffer, index)
	}

	this.id++

	return this.id - 1
}

func (this *SnapshotArray) Get(index int, snap_id int) int {
	if snap_id > this.id {
		return -1
	}

	var result int
	l := len(this.memory[index])

	for i := l - 1; i >= 0; i-- {
		if this.memory[index][i][1] <= snap_id {
			result = this.memory[index][i][0]
			break
		}
	}

	return result
}
