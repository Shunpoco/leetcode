use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn schedule_course(courses: Vec<Vec<i32>>) -> i32 {
        let mut courses = courses.iter().map(|c| (c[1], c[0])).collect::<Vec<_>>();
        courses.sort();
        
        let mut bp = BinaryHeap::new();
        let mut start = 0;
        
        for &(lastday, time) in courses.iter() {
            start += time;
            bp.push(time);
            while start > lastday {
                start -= bp.pop().unwrap();
            }
        }
        
        bp.len() as i32
    }
}

fn main() {
    assert_eq!(Solution::schedule_course(vec![vec![1, 2]]), 1);
}
