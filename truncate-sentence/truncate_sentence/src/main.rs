struct Solution {}

impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        s.split_whitespace().collect::<Vec<&str>>()[..(k as usize)].join(" ")
    }
}

fn main() {
    assert_eq!(Solution::truncate_sentence("How are you doing now".to_string(), 4), "How are you doing".to_string());
}
