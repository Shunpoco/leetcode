struct Solution;
impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        if num_friends == 1 {
            return word;
        }

        let max_len = word.len() - (num_friends as usize) + 1;

        let mut result = String::new();
        for i in 0..word.len() {
            let w = if i+max_len > word.len() {
                &word[i..]
            } else {
                &word[i..i+max_len]
            };

            let w = w.to_string();

            if w > result {
                result = w;
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
        let word = String::from("dbca");
        let num_friends = 2;

        let result = Solution::answer_string(word, num_friends);

        assert_eq!("dbc".to_string(), result);
    }

    #[test]
    fn second() {
        let word = String::from("gggg");
        let num_friends = 4;

        let result = Solution::answer_string(word, num_friends);

        assert_eq!("g".to_string(), result);
    }

    #[test]
    fn third() {
        let word = String::from("gh");
        let num_friends = 1;

        let result = Solution::answer_string(word, num_friends);

        assert_eq!("gh".to_string(), result);
    }
}
