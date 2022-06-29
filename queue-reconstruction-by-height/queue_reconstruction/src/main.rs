struct Solution;
impl Solution {
    pub fn reconstruct_queue(mut people: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        people.sort();
        people.sort_by(|a, b| b[0].cmp(&a[0]));
        
        let mut stack1 = vec![];
        let mut stack2 = vec![];
            
        for p in people.iter() {
            while stack1.len() > p[1] as usize {
                stack2.push(stack1.pop().unwrap());
            }
            stack1.push(p);
            while stack2.len() > 0 {
                stack1.push(stack2.pop().unwrap());
            }
        }

        let mut result = vec![];
        
        for p in stack1.iter() {
            result.push((*p).clone());
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::reconstruct_queue(vec![vec![7,0],vec![4,4],vec![7,1],vec![5,0],vec![6,1],vec![5,2]]), vec![vec![5,0], vec![7,0], vec![5,2], vec![6,1], vec![4,4], vec![7,1]]);
}
