struct Solution;
impl Solution {
    pub fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
        g.sort();
        s.sort();
        
        let mut count = 0;
        let mut i_s = 0usize;
        let mut i_g = 0usize;
        
        while i_g < g.len() && i_s < s.len() {
            if g[i_g] <= s[i_s] {
                count += 1;
                i_g += 1;
            }
            i_s += 1;
        }
        
        return count
    }
}

fn main() {
    assert_eq!(Solution::find_content_children(vec![1,2,3], vec![1,1]), 1);
}
