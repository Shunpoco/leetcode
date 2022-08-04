package main

func mirrorReflection(p int, q int) int {
    m, n := q, p
    
    for m%2 == 0 && n%2 == 0 {
        m /= 2
        n /= 2
    }
    
    if m%2 == 0 && n%2 == 1 {
        return 0
    } else if m%2 == 1 && n%2 == 1 {
        return 1
    } else if m%2 == 1 && n%2 == 0 {
        return 2
    }
    
    return -1    
}
