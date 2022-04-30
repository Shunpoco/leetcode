struct Solution;
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut mem = vec![0;cost.len()+1];
        for i in 0..mem.len() {
            if i == 0 || i == 1 {
                mem[i] = 0;
            } else {
                mem[i] = std::cmp::min(mem[i-2]+cost[i-2], mem[i-1]+cost[i-1]);
            }
        }
        
        mem[mem.len()-1]
    }
}

fn main() {
    assert_eq!(Solution::min_cost_climbing_stairs(vec![10,15,20]), 15);
}
