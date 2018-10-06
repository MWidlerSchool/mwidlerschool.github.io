from linked_list_link import LLLink

class LLObj():
    """Linked list object"""
    
    def __init__(self, data = None):
        """Initializer."""
        self.head = LLLink(data)
        self.head.next = self.head
        self.head.previous = self.head
        
        
    def findData(self, data):
        """Searches the list for the desired data. Returns the FIRST link which holds it, or None."""
        curLink = self.head
        returnVal = None
        if curLink.data == data:
            returnVal = curLink
        else:
            while curLink.data != data:
                curLink = curLink.next
                if curLink.data == data:
                    returnVal = curLink
        return returnVal
        
        
    def insertBefore(self, newData, oldData = None):
        """Insert before the chosen data, or at the front of the list if None is passed, 
        or append to the end if no matching data. If inserting before the head node, the new node 
        is set to the head."""
        newLink = LLLink(newData)
        if oldData == None:
            self.head.insertBefore(newLink)
            self.head = newLink
        else:
            desiredLink = self.findData(oldData)
            if desiredLink != None:
                desiredLink.insertBefore(newLink)
                if desiredLink == self.head:
                    self.head = newLink
            else:
                self.head.insertBefore(newLink)
    
    
    def insertAfter(self, newData, oldData = None):
        """Insert after specified data, or at the end of the list if data == None or not present."""
        newLink = LLLink(newData)
        if oldData == None:
            self.head.insertBefore(newLink)
        else:
            desiredLink = self.findData(oldData)
            if desiredLink != None:
                desiredLink.insertAfter(newLink)
            else:
                self.head.insertBefore(newLink)
    
    
    def getList(self):
        """Returns the LinkedList as a standard Python List."""
        curLink = self.head
        returnVal = []
        returnVal.append(curLink.data)
        curLink = curLink.next
        while curLink != self.head:
            returnVal.append(curLink.data)
            curLink = curLink.next
        return returnVal
            
if __name__ == "__main__":      
    listObj = LLObj(1)
    listObj.insertAfter(2)
    listObj.insertAfter(3)
    listObj.insertAfter(4)
    listObj.insertBefore(0)
    listObj.insertAfter(2.5, 2)
    listObj.insertBefore(-1, 0)
    print(listObj.getList())