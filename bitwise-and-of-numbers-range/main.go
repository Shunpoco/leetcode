package main

func rangeBitwiseAnd(left int, right int) int {
    result := 0
    
    for left > 0 && right > 0 {
        b_l := 1
        for b_l <= left {
            b_l *= 2
        }
        if b_l > left {
            b_l /= 2
        }
        b_r := 1
        for b_r < right {
            b_r *= 2
        }
        if b_r > right {
            b_r /= 2
        }
        
        if b_l != b_r {
            break
        }
        result += b_l
        left -= b_l
        right -= b_r
    }
    
    return result
}
