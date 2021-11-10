struct Solution {}

impl Solution {
    pub fn to_lower_case(s: String) -> String {
        s.chars().map(|x| x.to_lowercase().to_string()).collect::<String>()        
    }
}

// impl Solution {
//     pub fn to_lower_case(s: String) -> String {
//         s.to_lowercase()
//     }
// }


fn main() {
    assert_eq!(Solution::to_lower_case("Hello".to_string()), "hello".to_string())
}
