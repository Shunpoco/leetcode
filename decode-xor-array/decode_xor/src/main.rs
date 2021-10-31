struct Solution {}

impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        let n = encoded.len() + 1;
        let mut arr = vec![first; n];
        
        let mut prev = first;
        for i in 1..n {
            let v = encoded[i-1] ^ prev;
            prev = v;
            arr[i] = v;
        }
        
        arr
    }
}

fn main() {
    assert_eq!(Solution::decode(vec![1,2,3], 1), vec![1, 0, 2, 1]);
}
