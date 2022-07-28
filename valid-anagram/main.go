package main

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    
    mem1 := make(map[int]int)
    mem2 := make(map[int]int)
    for _, v := range s {
        mem1[int(v)]++
    }
    for _, v := range t {
        mem2[int(v)]++
    }
    
    for k, v := range mem1 {
        if v2, ok := mem2[k]; !ok || v != v2 {
            return false
        }
    }
    
    return true
}
