struct Solution;
impl Solution {
    pub fn divide(mut dividend: i32, mut divisor: i32) -> i32 {        
        let positive = (dividend < 0) == (divisor < 0);
        let mut result = 0;
        
        if dividend > 0 {
            dividend = -dividend;
        }
        
        if divisor > 0 {
            divisor = -divisor;
        }
        
        while dividend <= divisor {
            let mut temp = divisor;
            let mut i = -1;
            
            while dividend <= temp {
                dividend -= temp;
                result += i;
                temp <<= 1;
                if temp >= 0 {
                    break;
                }
                i <<= 1;
            }
        }
        
        if positive {
            if result == i32::MIN {
                result = i32::MAX;
            } else {
                result = -result;
            }
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::divide(10, -3), -3);
}
