class TreeNode:
    def __init__(self, key, val) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lruMap = {}
        self.dummyStart = TreeNode(-1,-1)
        self.dummyEnd = TreeNode(-1, -1)
        self.dummyStart.next = self.dummyEnd
        self.dummyEnd.prev = self.dummyStart

    def moveToEnd(self, nodeToReturn: TreeNode) -> None:
        nodeToReturn.prev.next = nodeToReturn.next
        nodeToReturn.next.prev = nodeToReturn.prev

        temp = self.dummyEnd.prev

        self.dummyEnd.prev = nodeToReturn
        nodeToReturn.next = self.dummyEnd
        nodeToReturn.prev = temp
        temp.next = nodeToReturn

    def get(self, key: int) -> int:
        if key in self.lruMap:
            nodeToReturn = self.lruMap[key]
        else:
            return -1

        self.moveToEnd(nodeToReturn)

        return nodeToReturn.val

    
    def put(self, key: int, value: int) -> None:
        if key in self.lruMap:
            self.lruMap[key].val = value
            self.moveToEnd(self.lruMap[key])
        else:
            if len(self.lruMap) == self.capacity:
                del self.lruMap[self.dummyStart.next.key]
                self.dummyStart.next = self.dummyStart.next.next
                self.dummyStart.next.prev = self.dummyStart
            
            self.lruMap[key] = TreeNode(key, value)
            newNode = self.lruMap[key]
            temp = self.dummyEnd.prev
            self.dummyEnd.prev = newNode
            newNode.next = self.dummyEnd
            newNode.prev = temp
            temp.next = newNode

            

        

        






        
