struct Solution {}

impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut wealth = 0i32;
        
        for account in accounts {
            let v = account.iter().sum();
            
            if v > wealth {
                wealth = v;
            }
        }
        
        wealth
    }
}

fn main() {
    println!("{}", Solution::maximum_wealth(vec![vec![1,2,3], vec![2,3,4]]));
}
