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
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        let mut head = head;    
        let mut result = 0i32;
        
        while head.is_some() {
            let v = head.unwrap();
            result *= 2;
            result += v.val;
            
            head = v.next;
        }
        
        result
    }
}


fn main() {
    let tail = ListNode::new(1);
    let mut mid = ListNode::new(0);
    mid.next = Some(Box::<ListNode>::new(tail));
    let mut head = ListNode::new(1);
    head.next = Some(Box::<ListNode>::new(mid));    

    assert_eq!(Solution::get_decimal_value(Some(Box::<ListNode>::new(head))), 5);
}
