use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn count_vowel_strings(n: i32) -> i32 {
        let mut memory: HashMap<(i32, i32), i32> = HashMap::new();
        
        dp(n, 5, &mut memory)
    }
}

fn dp(n: i32, s: i32, memory: &mut HashMap<(i32, i32), i32>) -> i32 {
    if let Some(v) = memory.get(&(n, s)) {
        return *v;
    }
    
    let mut result = 0i32;
    if n == 0 {
        result = 1;
    } else if s == 1 {
        result = 1;
    } else {
        for i in 0..s {
            result += dp(n-1, s-i, memory);
        }
    }
    
    memory.insert((n, s), result);
    
    result
}


fn main() {
    assert_eq!(Solution::count_vowel_strings(50), 316251);
}
