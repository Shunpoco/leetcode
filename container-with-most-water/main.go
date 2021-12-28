func maxArea(height []int) int {
    n := len(height)
    
    start, end := 0, n-1
    largest := 0
    
    for {
        if start >= end {
            break
        }
        
        m := height[start]
        if height[end] < m {
            m = height[end]
        }
        
        container := m * (end-start)
        
        if container > largest {
            largest = container
        }
        
        if height[start] > height[end] {
            end = end - 1
        } else {
            start = start + 1
        }
    }
    
    return largest
}
