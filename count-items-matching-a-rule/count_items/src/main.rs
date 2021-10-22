struct Solution {}

impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        let mut result = 0i32;
        let rule_key: &str = &rule_key;
        
        let key: usize;
        match rule_key {
            "type" => key = 0,
            "color" => key = 1,
            "name" => key = 2,
            _ => return result,
        }
        
        for item in items {
            if item[key] == rule_value {
                result += 1;
            }
            
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::count_matches(
        vec![
            vec![String::from("phone"), String::from("blue"), String::from("pixel")],
            vec![String::from("computer"), String::from("silver"), String::from("lenovo")],
            vec![String::from("phone"), String::from("gold"), String::from("iphone")],
        ],
        String::from("color"),
        String::from("silver"),
    ), 1);
}
