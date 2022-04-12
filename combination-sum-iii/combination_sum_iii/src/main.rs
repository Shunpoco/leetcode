struct Solution;
impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let mut stack = vec![vec![]];
        
        let mut output = vec![];
        while stack.len() > 0 {
            let cur = stack.pop().unwrap();
            if cur.len() as i32 == k {
                if cur.iter().sum::<i32>() == n {
                    output.push(cur.clone());
                }
                continue;
            }
            let start = if cur.len() > 0 { cur[cur.len()-1] } else { 0 };
            for i in start+1..10 {
                let mut t = cur.clone();
                t.push(i);
                stack.push(t);
            }
        }
        
        output
    }
}

fn main() {
    assert_eq!(Solution::combination_sum3(3, 7), vec![vec![1,2,4]]);
}
