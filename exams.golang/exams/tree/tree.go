package tree

import (
	"fmt"

	"exams.golang/utils/arrays"
	"github.com/gofiber/fiber/v2"
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
func doBuildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	if len(preorder) == 1 {
		return NewTreeNode(preorder[0])
	}

	rootVal := preorder[0]
	root := NewTreeNode(rootVal)

	rootInorderIndex := arrays.IndexOf(inorder, rootVal)

	var leftTreeInorder, leftTreePreorder, rightTreeInorder, rightTreePreorder []int

	if rootInorderIndex != 0 {
		leftTreeInorder = inorder[:rootInorderIndex]
		leftTreePreorder = preorder[1:(len(leftTreeInorder) + 1)]
	}

	if rootInorderIndex != (len(inorder) - 1) {
		rightTreeInorder = inorder[(rootInorderIndex + 1):]
		rightTreePreorder = preorder[(1 + len(leftTreeInorder)):]
	}

	root.Left = doBuildTree(leftTreePreorder, leftTreeInorder)
	root.Right = doBuildTree(rightTreePreorder, rightTreeInorder)

	return root
}

func BuildTree(c *fiber.Ctx) error {
	data := map[string][]int{}
	if err := c.BodyParser(&data); err != nil {
		return err
	}

	fmt.Println("BuildTree inputs =", data)
	tree := doBuildTree(data["preorder"], data["inorder"])

	return c.JSON(tree)
}
