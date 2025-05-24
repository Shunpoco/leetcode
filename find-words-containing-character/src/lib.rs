struct Solution;

impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let mut result = Vec::new();

        for (i, word) in words.iter().enumerate() {
            if word.contains(x) {
                result.push(i as i32);
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let words = vec!["leet".to_string(), "code".to_string()];
        let x = 'e';

        let result = Solution::find_words_containing(words, x);

        assert_eq!(result, vec![0, 1]);
    }

    #[test]
    fn second() {
        let words = vec!["abc".to_string(), "bcd".to_string(), "aaaa".to_string(), "cbc".to_string()];
        let x = 'a';

        let result = Solution::find_words_containing(words, x);

        assert_eq!(result, vec![0, 2]);
    }

    #[test]
    fn third() {
        let words = vec!["abc".to_string(), "bcd".to_string(), "aaaa".to_string(), "cbc".to_string()];
        let x = 'z';

        let result = Solution::find_words_containing(words, x);

        assert_eq!(result, vec![]);
    }
}
