package tree

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func NewTreeNode(val int) *TreeNode {
	node := new(TreeNode)
	node.Val = val

	return node
}

/*
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

eg1:

	  3
	 / \
	9  20
	  /  \
	 15   7

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

eg2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
*/
func BuildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	if len(preorder) == 1 {
		return NewTreeNode(preorder[0])
	}

	rootVal := preorder[0]
	root := NewTreeNode(rootVal)

	rootValInorderIndex := 0
	for i, v := range inorder {
		if rootVal == v {
			rootValInorderIndex = i
			break
		}
	}

	var inorderLeftValues, preorderLeftValues, inorderRightValues, preorderRightValues []int

	if rootValInorderIndex != 0 {
		inorderLeftValues = inorder[:rootValInorderIndex]
		preorderLeftValues = preorder[1:(len(inorderLeftValues) + 1)]
	}

	if rootValInorderIndex != (len(inorder) - 1) {
		inorderRightValues = inorder[(rootValInorderIndex + 1):]
		preorderRightValues = preorder[(1 + len(inorderLeftValues)):]
	}

	fmt.Println("inorderLeftValues, preorderLeftValues = ", inorderLeftValues, preorderLeftValues)
	fmt.Println("inorderRightValues, preorderRightValues = ", inorderRightValues, preorderRightValues)

	root.Left = BuildTree(inorderLeftValues, preorderLeftValues)
	root.Right = BuildTree(inorderRightValues, preorderRightValues)

	return root
}
