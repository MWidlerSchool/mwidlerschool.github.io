import unittest
from bsnode import BSNode
from bstree import BSTree
import random

class TestBST(unittest.TestCase):
    """Unit testing class for binary search tree."""

    def test_node(self):
        testNode = BSNode(10)
        self.assertEqual(testNode.data, 10)
        self.assertEqual(testNode.left, None)
        self.assertEqual(testNode.right, None)
        self.assertFalse(testNode.left)
        self.assertFalse(testNode.right)
        testNode.add(5)
        testNode.add(20)
        self.assertEqual(testNode.left.data, 5)
        self.assertEqual(testNode.right.data, 20)
        self.assertTrue(testNode.left)
        self.assertTrue(testNode.right)
        
    def testTree(self):
        testTree = BSTree()
        testTree.add(5)
        testTree.add(3)
        testTree.add(1)
        testTree.add(2)
        testTree.add(4)
        self.assertEqual(testTree.getAsList(), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()