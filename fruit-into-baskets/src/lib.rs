struct Solution;
impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        // The first element represents a fruit,
        // And the second one counts the amount.
        let mut new_fruits: Vec<(i32, i32)> = vec![];

        let mut current_fruit = -1;
        let mut count = 0;
        for &fruit in fruits.iter() {
            if fruit == current_fruit {
                count += 1;
            } else if current_fruit == -1 {
                current_fruit = fruit;
                count = 1;
            } else {
                new_fruits.push((current_fruit, count));
                current_fruit = fruit;
                count = 1;
            }
        }

        new_fruits.push((current_fruit, count));

        if new_fruits.len() == 1 {
            return new_fruits[0].1;
        }

        let mut right = 1;
        let mut baskets = vec![new_fruits[0].0, new_fruits[right].0];
        let mut t= new_fruits[0].1 + new_fruits[right].1;
        let mut result = 0;

        while right < new_fruits.len()-1 {
            right += 1;

            if new_fruits[right].0 != baskets[0] {
                if t > result {
                    result = t;
                }

                baskets = vec![baskets[1], new_fruits[right].0];
                t = new_fruits[right-1].1 + new_fruits[right].1;
            } else {
                baskets = vec![baskets[1], new_fruits[right].0];
                t += new_fruits[right].1;
            }
        }

        if t > result {
            result = t;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let fruits = vec![1, 2, 1];
        let result = Solution::total_fruit(fruits);

        assert_eq!(3, result);
    }

    #[test]
    fn second() {
        let fruits = vec![0, 1, 2, 2];
        let result = Solution::total_fruit(fruits);

        assert_eq!(3, result);
    }

    #[test]
    fn third() {
        let fruits = vec![1, 2, 3, 2, 2];
        let result = Solution::total_fruit(fruits);

        assert_eq!(4, result);
    }

    #[test]
    fn fourth() {
        let fruits = vec![0];
        let result = Solution::total_fruit(fruits);

        assert_eq!(1, result);
    }

    #[test]
    fn fifth() {
        let fruits = vec![3, 3, 3, 3, 3, 3];
        let result = Solution::total_fruit(fruits);

        assert_eq!(6, result);
    }
}
