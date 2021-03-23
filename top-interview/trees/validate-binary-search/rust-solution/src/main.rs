use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

struct Solution {}

impl Solution {
    // reference: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/discuss/343961/Rust-Solution
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::valid(root, std::i64::MIN, std::i64::MAX)
    }

    fn valid(node: Option<Rc<RefCell<TreeNode>>>, min: i64, max: i64) -> bool {
        if let Some(node) = node {
            if node.borrow().val as i64 <= min || node.borrow().val as i64 >= max {
                return false;
            }
            return Self::valid(node.borrow().left.clone(), min, node.borrow().val as i64) &&
                Self::valid(node.borrow().right.clone(), node.borrow().val as i64, max);
        }
        true
    }
}

fn main() {}

#[cfg(test)]
mod test {
    // TODO: write unittest
    use super::*;
    #[test]
    fn testIsValidBst1() {
        // let mut testCase: TreeNode = TreeNode::new(2);
        // testCase.borrow().left = TreeNode::new(1);

    }
}