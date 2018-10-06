import random
from bstree import BSTree

selection = input("I will return the k smallest number from a list. What value should I use for k (1-15)?")
selection = int(selection) - 1

tree = BSTree()
for i in range(20):
    tree.add(random.randint(0, 100))
treeList = tree.getAsList()

print("The value of k is {}.".format(treeList[selection]))
print(treeList)