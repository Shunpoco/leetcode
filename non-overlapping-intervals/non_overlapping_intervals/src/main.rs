struct Solution;
impl Solution {
    pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort();
        
        // println!("{:?}", intervals);
        
        let mut remove = vec![0;intervals.len()];
        let mut cur = 0usize;
        for i in 1..intervals.len() {
            let v = &intervals[i];
            let end = intervals[cur][1];
            if end > v[0] && end < v[1] {
                remove[i] = 1;
            } else if end > v[0] {
                remove[cur] = 1;
                cur = i;
            } else {
                cur = i;
            }
        }
        
        // println!("{:?}", remove);
        
        remove.iter().sum::<i32>()
    }
}

fn main() {
    assert_eq!(Solution::erase_overlap_intervals(vec![vec![1,2],vec![2,3],vec![3,4],vec![1,3]]), 1);
}
