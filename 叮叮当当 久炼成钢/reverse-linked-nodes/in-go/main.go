package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

// func

func ReverseList(pHead *ListNode) *ListNode {
	// write code here
	if pHead == nil || pHead.Next == nil {
		return pHead
	}

	var preNode *ListNode = pHead
	var nextNode *ListNode = pHead.Next
	var curNode *ListNode
	for nextNode != nil {
		fmt.Println(nextNode)
		fmt.Println("nextNode == nil: ", nextNode == nil)
		curNode = nextNode
		nextNode = curNode.Next
		curNode.Next = preNode
		preNode = curNode
	}
	fmt.Println("return curNode: ", curNode)
	return curNode
}

func main() {

}
