struct Solution;
impl Solution {
    pub fn get_sum(mut a: i32, mut b: i32) -> i32 {        
        Self.add(a, b)
    }

    fn add(self, mut a: i32, mut b: i32) -> i32 {
        let mut result = 0i32;
        
        let mut idx = 0i32;
        let mut c = 0i32;
        
        for idx in 0..32 {
            let a_ = a&1;
            let b_ = b&1;
            
            let v = a_^b_;
            let c_ = if a_&b_ == 1 { 1 } else { 0 };
            
            let n =  (v^c)<<idx;
            let c__ = if v&c == 1 { 1 } else { 0 };
            
            c = c_|c__;
            
            result |= n;
            
            a >>= 1;
            b >>= 1;
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::get_sum(1, 2), 3);
}
