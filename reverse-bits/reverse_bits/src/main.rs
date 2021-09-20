struct Solution {}

impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut x = x;
        let mut res = 0u32;
        
        for i in 0..32 {
            let v = (x & 1) << (31-i);
            res = res | v;
            x = x >> 1;
        }
        
        res
    }
}

fn main() {
    assert_eq!(Solution::reverse_bits(43261596), 964176192);
    assert_eq!(Solution::reverse_bits(4294967293), 3221225471);
}

#[test]
fn test_reverse_bits() {
    assert_eq!(Solution::reverse_bits(43261596), 964176192);
    assert_eq!(Solution::reverse_bits(4294967293), 3221225471);
}
