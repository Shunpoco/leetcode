impl Solution {
  pub fn reverse(x: i32) -> i32 {
    let mut digit: i64 = 1;
    let mut target: i64 = (x as i64);
    if x < 0 {
      digit = -1;
      target = -1 * target;
    }
    let mut vec = Vec::new();
    let max: i64 = (2 as i64).pow(31) - 1;
    let min: i64 = -1 * (2 as i64).pow(31);
    while target != 0 {
      let d: i64 = target % 10;
      vec.push(d);
      target = target / 10;
    }
    let mut r: i64 = 0;
    for i in  0..vec.len() {
      let t: i64 = vec[vec.len()-1-i] * ((10 as u32).pow((i as u32)) as i64);
      r += t;
    }

    r = digit * r;

    if r > max || r < min {
      r = 0;
    }
    return r as i32;
  }
}