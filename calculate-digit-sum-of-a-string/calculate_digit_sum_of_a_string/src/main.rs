struct Solution;
impl Solution {
    pub fn digit_sum(s: String, k: i32) -> String {
        let mut s: Vec<char> = s.chars().collect();
        while s.len() > k as usize {
            s = exec(&s, k);
        }
        
        s.iter().collect::<String>()
    }
}

fn exec(s: &Vec<char>, k: i32) -> Vec<char> {
    let mut result = vec![];
    let mut counter = 0i32;
    let mut sum = 0i32;
    for &c in s.iter() {
        sum += c as i32 - 48;
        counter += 1;
        if counter == k {
            append(&mut result, sum);
            counter = 0;
            sum = 0;
        }
    }
    
    if counter != 0 {
        append(&mut result, sum);
    }
    
    result
}

fn append(result: &mut Vec<char>, mut sum: i32) {
    if sum < 10 {
        result.push((sum as u8 + 48) as char);
    } else {
        append(result, sum/10);
        sum %= 10;
        result.push((sum as u8 + 48) as char);
    }
}

fn main() {
    assert_eq!(Solution::digit_sum("11111222223".to_string(), 3), "135".to_string());
}
