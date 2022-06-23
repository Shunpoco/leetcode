struct Solution;
impl Solution {
    pub fn find_lu_slength(a: String, b: String) -> i32 {
        if a == b {
            return -1;
        }
        
        let na = a.len() as i32;
        let nb = b.len() as i32;
        
        return if na >= nb { na } else { nb };        
    }
}

fn main() {
    assert_eq!(Solution::find_lu_slength("aaa".to_string(), "bbb".to_string()), 3);
}
