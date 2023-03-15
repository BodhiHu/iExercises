package linked_list

import (
	"fmt"

	"github.com/gofiber/fiber/v2"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func NewNode(val int, next *ListNode) *ListNode {
	node := new(ListNode)
	node.Val = val
	node.Next = next
	return node
}

func NewNodeList(values []int) *ListNode {
	if len(values) == 0 {
		return nil
	}

	var rootNode *ListNode = nil
	var lastNode *ListNode = nil
	for _, v := range values {
		curNode := NewNode(v, nil)
		if rootNode == nil {
			rootNode = curNode
		}
		if lastNode != nil {
			lastNode.Next = curNode
		}

		lastNode = curNode
	}

	return rootNode
}

func ReverseList(pHead *ListNode) *ListNode {
	if pHead == nil {
		return pHead
	}

	arr := []*ListNode{}
	for curNode := pHead; curNode != nil; curNode = curNode.Next {
		arr = append(arr, curNode)
	}
	for i := len(arr) - 1; i > 0; i-- {
		arr[i].Next = arr[i-1]
		if i == 1 {
			arr[0].Next = nil
		}
	}

	return arr[len(arr)-1]
}

func GetListValues(pHead *ListNode) []int {
	values := []int{}

	for cur := pHead; cur != nil; cur = cur.Next {
		values = append(values, cur.Val)
	}

	return values
}

func PrintList(prefix string, pHead *ListNode) {
	fmt.Print(prefix)
	curNode := pHead
	for curNode != nil {
		fmt.Print(curNode, "\n")
		curNode = curNode.Next
	}
}

func ReverseLinkedListToValues(c *fiber.Ctx) error {
	// values := []int{1, 2, 3, 4, 5}

	values := new([]int)
	if err := c.BodyParser(values); err != nil {
		return err
	}

	nodeList := NewNodeList(*values)
	PrintList("nodeList = \n", nodeList)

	revertedList := ReverseList(nodeList)
	PrintList("\nrevertedList = \n", revertedList)

	reversedValues := GetListValues(revertedList)
	fmt.Print("\nreversedValues = \n", reversedValues)

	return c.JSON(reversedValues)
}
