// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution {}

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut one = l1.unwrap();
        let mut two = l2.unwrap();
        let mut root = ListNode::new(0);
        
        let mut res = Solution::make_node(one.val + two.val);
        root.next.get_or_insert(Box::new(res.0));
        
        let mut curr = &mut root.next;
        
        while one.next.is_some() || two.next.is_some() {
            match curr {
                None => break,
                Some(now) => {
                    one = one.next.or(Some(Box::new(ListNode::new(0)))).unwrap();
                    two = two.next.or(Some(Box::new(ListNode::new(0)))).unwrap();
                    
                    res = Solution::make_node(one.val + two.val + res.1);
                    
                    now.next.get_or_insert(Box::new(res.0));
                    curr = &mut now.next;
                }
            }
        }
        
        if res.1 > 0 {
            if let Some(now) = curr {
                now.next.get_or_insert(Box::new(ListNode::new(res.1)));
            }
        }
        
        root.next
    }
    
    fn make_node(mut result: i32) -> (ListNode, i32) {
        let single;
        if result > 9 {
            single = 1;
            result = result - 10;
        } else {
            single = 0;
        }
        (ListNode::new(result), single)
    }
}

fn main() {
    println!("{:?}", Solution::add_two_numbers(Some(Box::new(ListNode::new(5))), Some(Box::new(ListNode::new(5)))));
}
