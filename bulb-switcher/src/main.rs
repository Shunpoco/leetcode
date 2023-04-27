struct Solution {}
impl Solution {
    pub fn bulb_switch(n: i32) -> i32 {
        if n == 0 {
            return n;
        }
        let mut b = 1;
        while b*b <= n {
            b += 1;
        }

        b -= 1;
        b
    }
}

fn main() {
    println!("{}", Solution::bulb_switch(3));
}
