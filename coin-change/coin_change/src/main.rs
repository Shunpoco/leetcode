use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut m = HashMap::new();
        m.insert(0, 0);
        
        dp(&coins, amount, &mut m)
    }
}

fn dp(coins: &Vec<i32>, amount: i32, memory: &mut HashMap<i32, i32>) -> i32 {
    if let Some(v) = memory.get(&amount) {
        return *v;
    }
    
    let mut count = -1;
    
    for &coin in coins {
        if amount >= coin {
            let v = dp(coins, amount-coin, memory);
            if v == -1 {
                continue;
            }
            if count == -1 || v+1 < count {
                count = v+1;
            }
        }
    }
    
    memory.insert(amount, count);
    
    count
}


fn main() {
    assert_eq!(Solution::coin_change(vec![1,2,5], 11), 3);
}
