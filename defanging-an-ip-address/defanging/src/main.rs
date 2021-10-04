struct Solution {}

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        address.replace(".", "[.]")
    }
}

fn main() {
    println!("{}", Solution::defang_i_paddr("192.168.11.1".to_string()));
}
