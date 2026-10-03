struct Solution;

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

impl Solution {
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut cur = dummy.as_mut();

        while !list1.is_none() && !list2.is_none() {
            let v1 = list1.as_ref().unwrap();
            let v2 = list2.as_ref().unwrap();

            if v1.val > v2.val {
                cur.next = Some(Box::new(ListNode::new(v2.val)));
                cur = cur.next.as_mut().unwrap();
                list2 = list2.unwrap().next;
            } else {
                cur.next = Some(Box::new(ListNode::new(v1.val)));
                cur = cur.next.as_mut().unwrap();
                list1 = list1.unwrap().next;
            }
        }

        while !list1.is_none() {
            let v1 = list1.as_ref().unwrap();
            cur.next = Some(Box::new(ListNode::new(v1.val)));
            cur = cur.next.as_mut().unwrap();
            list1 = list1.unwrap().next;
        }

        while !list2.is_none() {
            let v2 = list2.as_ref().unwrap();
            cur.next = Some(Box::new(ListNode::new(v2.val)));
            cur = cur.next.as_mut().unwrap();
            list2 = list2.unwrap().next;
        }

        dummy.next
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn to_listnode(list: Vec<i32>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut cur = dummy.as_mut();

        for v in list {
            cur.next = Some(Box::new(ListNode::new(v)));
            cur = cur.next.as_mut().unwrap();
        }

        dummy.next
    }

    #[test]
    fn first() {
        let list1 = to_listnode(vec![1,2,4]);
        let list2 = to_listnode(vec![1,3,4]);
        let result = to_listnode(vec![1,1,2,3,4,4]);

        assert_eq!(result, Solution::merge_two_lists(list1, list2));        
    }

    #[test]
    fn second() {
        let list1 = to_listnode(vec![]);
        let list2 = to_listnode(vec![]);
        let result = to_listnode(vec![]);

        assert_eq!(result, Solution::merge_two_lists(list1, list2));
    }

    #[test]
    fn third() {
        let list1 = to_listnode(vec![]);
        let list2 = to_listnode(vec![1]);
        let result = to_listnode(vec![1]);

        assert_eq!(result, Solution::merge_two_lists(list1, list2));
    }
}
