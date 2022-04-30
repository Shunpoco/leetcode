struct Solution;
// impl Solution {
//     pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
//         let mut mem = vec![0;cost.len()+1];
//         for i in 0..mem.len() {
//             if i == 0 || i == 1 {
//                 mem[i] = 0;
//             } else {
//                 mem[i] = std::cmp::min(mem[i-2]+cost[i-2], mem[i-1]+cost[i-1]);
//             }
//         }
        
//         mem[mem.len()-1]
//     }
// }

impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let (mut v1, mut v2, mut v3) = (0, 0, 0);
        
        for i in 2..cost.len()+1 {
            v3 = std::cmp::min(v2+cost[i-1], v1+cost[i-2]);            
            v1 = v2;
            v2 = v3;
        }        
        v3
    }
}

fn main() {
    assert_eq!(Solution::min_cost_climbing_stairs(vec![10,15,20]), 15);
}
