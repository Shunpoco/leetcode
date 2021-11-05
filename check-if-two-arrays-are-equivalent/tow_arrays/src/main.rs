struct Solution {}

impl Solution {
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        let word1 = word1.join("");
        let word2 = word2.join("");
        
        word1 == word2
    }
}

fn main() {
    assert_eq!(Solution::array_strings_are_equal(vec!["ab".to_string(), "c".to_string()], vec!["abc".to_string()]), true);
}
