struct Solution {}

impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        let mut word: Vec<char> = word.chars().collect();
        
        let mut idx = 0usize;
        
        for i in 0..word.len() {
            if word[i] == ch {
                idx = i;
                break;
            }
        }
        
        for i in 0..idx/2+1 {
            let temp = word[i];
            word[i] = word[idx-i];
            word[idx-i] = temp;
        }
        
        word.into_iter().collect()
    }
}

fn main() {
    assert_eq!(Solution::reverse_prefix("abcdefd".to_string(), 'd'), "dcbaefd".to_string());
}
