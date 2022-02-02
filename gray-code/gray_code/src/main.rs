struct Solution;

impl Solution {
    pub fn gray_code(n: i32) -> Vec<i32> {
        if n == 0 {
            return vec![0];
        }
        
        let mut geta = 1i32;
        for _ in 0..(n-1) {
            geta *= 2;
        }
        
        let mut res1 = Solution::gray_code(n-1);
        let res2 = res1.clone();
        
        for i in 0..res1.len() {
            let v = res2[res2.len()-i-1] + geta;
            res1.push(v);
        }
        
        return res1;
        
    }
    
}


fn main() {
    assert_eq!(Solution::gray_code(2), vec![0,1,3,2]);
}
