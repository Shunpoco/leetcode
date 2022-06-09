package main

func twoSum(numbers []int, target int) []int {
    n := len(numbers)
    for i:=0; i<n; i++ {
        t := target - numbers[i]
        cur := (n-i)/2
        min := 0
        max := n-i
        for cur < max && cur >= min {
            v := numbers[cur+i]
            if v == t {
                return []int{i+1, cur+i+1}
            } else if v > t {
                if cur == min {
                    break
                }
                max = cur
                cur = (max+min)/2
            } else {
                if cur+1 == max {
                    break
                }
                min = cur+1
                cur = (max+min)/2
            }
        }
    }

    return []int{}
}
