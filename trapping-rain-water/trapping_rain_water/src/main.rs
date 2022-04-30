struct Solution;
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut count = 0i32;
        
        let mut stack = vec![];
        let mut t_stack = vec![];
        let mut max = 0;
        
        for &h in height.iter() {
            if stack.len() == 0 {
                max = h;
                stack.push((h, max));
            } else {                
                while stack.len() > 0 && stack[stack.len()-1].0 < h {
                    let v = stack.pop().unwrap();
                    count += std::cmp::min(h-v.0, v.1-v.0);
                    t_stack.push((h, v.1));
                    if v.0 == v.1 {
                        break;
                    }
                }
                while t_stack.len() > 0 {
                    let v = t_stack.pop().unwrap();
                    stack.push(v);
                }

                if h > max {
                    max = h;
                }
                stack.push((h, max))
            }
        }
        
        count
    }
}

fn main() {
    assert_eq!(Solution::trap(vec![0,1,0,2,1,0,1,3,2,1,2,1]), 6);
}
