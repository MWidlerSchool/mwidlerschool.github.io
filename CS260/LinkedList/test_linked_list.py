import unittest
from linked_list_link import LLLink
from linked_list_obj import LLObj
from better_stack import BetterStack
from better_queue import BetterQueue

class TestLinkedList(unittest.TestCase):
    """Unit testing class for linked list class, as well as BetterStack and BetterQueue."""

    def test_link(self):
        testLink = LLLink("A")
        self.assertEqual(testLink.next, testLink)
        self.assertEqual(testLink.previous, testLink)
        self.assertEqual(testLink.data, "A")
    
    def test_list(self):
        testTree = LLObj("C")
        testTree.insertAfter("D")
        testTree.insertAfter("F")
        testTree.insertBefore("B")
        testTree.insertAfter("E", "D")
        testTree.insertBefore("A", "B")
        self.assertEqual(testTree.getList(), ["A", "B", "C", "D", "E", "F"])
        
    def testQueue(self):
        testQueue = BetterQueue("Start")
        for i in range(5):
            testQueue.push(chr(65 + i))
        testQueue.push("End")
        self.assertEqual(len(testQueue), 7)
        self.assertEqual(str(testQueue), "['Start', 'A', 'B', 'C', 'D', 'E', 'End']")
        self.assertEqual(testQueue.pop(), "Start")
        testQueue.clear()
        self.assertEqual(len(testQueue), 0)
        with self.assertRaises(IndexError): testQueue.pop()
        
    def testStack(self):
        testStack = BetterStack("Start")
        for i in range(5):
            testStack.push(chr(65 + i))
        testStack.push("End")
        self.assertEqual(len(testStack), 7)
        self.assertEqual(str(testStack), "['Start', 'A', 'B', 'C', 'D', 'E', 'End']")
        self.assertEqual(testStack.pop(), "End")
        testStack.clear()
        self.assertEqual(len(testStack), 0)
        with self.assertRaises(IndexError): testStack.pop()


if __name__ == "__main__":
    unittest.main()