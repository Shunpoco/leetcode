use std::cmp::Reverse;

struct Solution;
impl Solution {
    pub fn max_envelopes(envelopes: Vec<Vec<i32>>) -> i32 {
        let mut envelopes = envelopes
            .iter()
            .map(|envelop| (envelop[0], Reverse(envelop[1])))
            .collect::<Vec<_>>();
        
        envelopes.sort_unstable();
        
        let mut dp = Vec::new();
        
        for &(_, Reverse(h)) in &envelopes {
            if let Some(i) = dp.binary_search(&h).err() {
                if i >= dp.len() {
                    dp.push(h);
                } else {
                    dp[i] = h;
                }
            }
        }
        
        dp.len() as i32
    }
}


fn main() {
    assert_eq!(Solution::max_envelopes(vec![vec![5,4], vec![6, 4], vec![6, 7], vec![2, 3]]), 3);
}
