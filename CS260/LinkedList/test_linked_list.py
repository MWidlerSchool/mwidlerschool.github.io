import unittest
from linked_list_link import LLLink
from linked_list_obj import LLObj
import random

class TestLinkedList(unittest.TestCase):
    """Unit testing class for linked list class."""

    def test_link(self):
        testLink = LLLink("A")
        self.assertEqual(testLink.next, testLink)
        self.assertEqual(testLink.previous, testLink)
        self.assertEqual(testLink.data, "A")
    
    def test_tree(self):
        testTree = LLObj("C")
        testTree.insertAfter("D")
        testTree.insertAfter("F")
        testTree.insertBefore("B")
        testTree.insertAfter("E", "D")
        testTree.insertBefore("A", "B")
        self.assertEqual(testTree.getList(), ["A", "B", "C", "D", "E", "F"])


if __name__ == "__main__":
    unittest.main()