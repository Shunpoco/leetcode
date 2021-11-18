struct Solution {}

impl Solution {
    pub fn flip_and_invert_image(image: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![];
        
        let len = image[0].len();
        
        for i in 0..len {
            let v = &image[i];
            let mut temp = vec![0; len];
            for j in 0..(len/2) {
                temp[j] = v[len-1-j]^1;
                temp[len-1-j] = v[j]^1;
            }
            if len % 2 != 0 {
                temp[len/2] = v[len/2]^1;
            }
            
            result.push(temp);
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::flip_and_invert_image(vec![vec![1,0,1], vec![0,1,0], vec![0,0,1]]), vec![vec![0,1,0], vec![1,0,1], vec![0,1,1]]);
}
