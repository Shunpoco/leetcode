func divide(dividend int, divisor int) int {
    positive := (dividend < 0) == (divisor < 0)
    
    MAX := 2147483647
    MIN := -2147483648
    
    if dividend > 0 {
        dividend = -dividend
    }
    if divisor > 0 {
        divisor = -divisor
    }
    
    result := 0
    
    for dividend <= divisor {
        temp := divisor
        i := 1
        for dividend <= temp {
            dividend -= temp
            result += i
            temp = temp << 1
            i = i << 1            
        }
    }
    
    if positive == false {
        result = -result
    }
   
    if result < MIN {
        result = MIN
    }
    
    if result > MAX {
        result = MAX
    }
    
    return result
    
}
