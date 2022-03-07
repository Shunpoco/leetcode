use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn find_words(words: Vec<String>) -> Vec<String> {
        let mut h1 = HashMap::new();
        for c in "qwertyuiop".chars().collect::<Vec<char>>() {
            h1.insert(c, true);
        }
        let mut h2 = HashMap::new();
        for c in "asdfghjkl".chars().collect::<Vec<char>>() {
            h2.insert(c, true);
        }
        let mut h3 = HashMap::new();
        for c in "zxcvbnm".chars().collect::<Vec<char>>() {
            h3.insert(c, true);
        }
        
        let mut result = vec![];
        let mut hit1 = true;
        let mut hit2 = true;
        let mut hit3 = true;
        for word in words {
            hit1 = true;
            hit2 = true;
            hit3 = true;
            let w:Vec<char> = word.as_str().to_lowercase().chars().collect();
            println!("{:?}", w);
            for &w_ in w.iter() {
                if !h1.contains_key(&w_) {
                    hit1 = false;
                }
                if !h2.contains_key(&w_) {
                    hit2 = false;
                }
                if !h3.contains_key(&w_) {
                    hit3 = false;
                }
            }
            if hit1 || hit2 || hit3 {
                result.push(word);
            }
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::find_words(vec!["Hello".to_string(), "Alaska".to_string(), "Dad".to_string(), "Peace".to_string()]), vec!["Alaska".to_string(), "Dad".to_string()]);
}
