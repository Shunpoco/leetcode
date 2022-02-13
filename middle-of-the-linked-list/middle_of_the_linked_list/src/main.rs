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

struct Solution;
impl Solution {
    pub fn middle_node(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l = 0usize;
        let mut cout = head.as_ref();
        
        while let Some(node) = cout {
            cout = node.next.as_ref();
            l += 1;
        }
        
        for _ in 0..l/2 {
            head = head.unwrap().next;
        }
        
        head
    }
}


fn main() {
    let list1 = Some(Box::new(ListNode::new(3)));
    let mut l2 = ListNode::new(2);
    l2.next = list1;
    let list2 = Some(Box::new(l2));
    let mut l3 = ListNode::new(1);
    l3.next = list2.clone();
    let list3 = Some(Box::new(l3));

    assert_eq!(
        Solution::middle_node(list3),
        list2,
    );
}
