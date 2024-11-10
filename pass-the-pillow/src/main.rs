struct Solution;
impl Solution {
    pub fn pass_the_pillow(n: i32, mut time: i32) -> i32 {
        let mut pos = 1;
        let mut go_right = true;

        while time > 0 {
            if go_right {
                pos += 1;
                if pos == n {
                    go_right = false;
                }
            } else {
                pos -= 1;
                if pos == 1 {
                    go_right = true;
                }
            }
            time -= 1;
        }

        pos
    }
}

fn main() {
    let n = 4;
    let time = 5;

    let got = Solution::pass_the_pillow(n, time);

    assert!(got == 2);

    println!("{}", got);
}
