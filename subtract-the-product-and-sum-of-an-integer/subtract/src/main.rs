struct Solution {}

impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 {
        let mut product = 1i32;
        let mut summation = 0i32;
        
        let mut n = n;
        
        while n != 0 {
            let v = n % 10;
            product *= v;
            summation += v;
            
            n = n / 10;
        }
        
        product - summation
    }
}


fn main() {
    assert_eq!(Solution::subtract_product_and_sum(234), 15);
}
