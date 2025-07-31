/**
 * Definition for singly-linked list.
 */

class ListNode {
  int val;
  ListNode next;

  ListNode() {
  }

  ListNode(int val) {
    this.val = val;
  }

  ListNode(int val, ListNode next) {
    this.val = val;
    this.next = next;
  }
}

class Solution {
  public int getDecimalValue(ListNode head) {
    int res = 0;
    if (head.val == 1)
      res = 1;

    ListNode curr = head.next;
    while (curr != null) {
      res = res * 2 + curr.val;
      curr = curr.next;
    }

    return res;
  }
}