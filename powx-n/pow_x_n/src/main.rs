struct Solution {}

impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        if n == 2 {
            return x * x;
        } else if n == 1 {
            return x;
        } else if n == 0 {
            return 1.0;
        }

        let mut x = x;
        let mut digit = 1;
        
        if n < 0 {
            x = 1.0 / x;
            digit = -1;
        }
        
        let odd: bool;
        
        if n % 2 != 0 {
            odd = true;
        } else {
            odd = false;
        }
        
        let result = Solution::my_pow(x, n/2*digit);
        if odd {
            return result * result * x;
        }
        
        result * result
    }
}


fn main() {
    assert_eq!(Solution::my_pow(2.00000, -2147483648), 0.0);
}
