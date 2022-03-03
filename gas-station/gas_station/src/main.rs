struct Solution;
impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let sum = |v: Vec<i32>| -> i32 {
            v.iter().sum::<i32>()
        };
        
        if sum(gas.clone()) < sum(cost.clone()) {
            return -1;
        }
        
        let mut total = 0;
        let mut start = 0;
        for i in 0..gas.len() {
            total += gas[i]-cost[i];
            if total < 0 {
                start = i+1;
                total = 0;
            }
        }
        
        start as i32
    }
}

fn main() {
    assert_eq!(Solution::can_complete_circuit(vec![1,2,3,4,5], vec![3,4,5,1,2]), 3);
}
