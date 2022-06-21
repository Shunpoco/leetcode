use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, mut ladders: i32) -> i32 {
        let mut costs = BinaryHeap::new();
        
        let mut counter = 0i32;
        let mut idx = 1usize;
        while idx < heights.len() {
            let mut diff = heights[idx] - heights[idx-1];
            if diff <= 0 {
                idx += 1;
                continue;
            }
            
            if counter + diff <= bricks {
                counter += diff;
                costs.push(diff);
            } else {
                if ladders > 0 {
                    ladders -= 1;
                    if costs.len() > 0 {
                        let v = *costs.peek().unwrap();
                        if v > diff {
                            costs.pop();
                            counter -= v;
                            counter += diff;
                            costs.push(diff);
                        }                        
                    }
                } else {
                    break;
                }
            }
            idx += 1;
        }
        
        idx as i32 - 1
    }
}

fn main() {
    assert_eq!(Solution::furthest_building(vec![4,2,7,6,9,14,12], 5, 1), 4);
}
