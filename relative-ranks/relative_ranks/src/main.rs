use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn find_relative_ranks(score: Vec<i32>) -> Vec<String> {
        let n = score.len();
        let mut heap = BinaryHeap::new();
        
        for (i, &s) in score.iter().enumerate() {
            heap.push((s, i));
        }
        
        let mut answer = vec!["".to_string();n];
        
        let mut idx = 0usize;
        while heap.len() > 0 {
            let v = heap.pop().unwrap();
            
            match idx {
                0 => {
                    answer[v.1] = "Gold Medal".to_string();
                },
                1 => {
                    answer[v.1] = "Silver Medal".to_string();
                },
                2 => {
                    answer[v.1] = "Bronze Medal".to_string();
                },
                _ => {
                    answer[v.1] = (idx+1).to_string();
                }
            }
            
            idx += 1;
        }
        
        answer
    }
}

fn main() {
    assert_eq!(
        Solution::find_relative_ranks(vec![5,4,3,2,1]),
        vec!["Gold Medal","Silver Medal","Bronze Medal","4","5"]
            .into_iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
    );
}
