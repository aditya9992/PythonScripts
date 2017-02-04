class Node: 
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

def intersectionNode(d, node1, node2):

    for i in range(d):
        if node1 == None:
            return -1
        node1 = node1.next
    
    while node1 != None and node2 != None:
        if node1 == node2:
            return node1.data
        node1 = node1.next
        node2 = node2.next
    
    return -1

def lenLL(node):
    count = 0
    current = node
    while current.next != None:
        count += 1
        current = current.next
    return count


head1 = Node(10)
head2 = Node(3)

newNode = Node(6)
head2.next = newNode

newNode = Node(9)
head2.next.next = newNode

newNode = Node(15)
head2.next.next.next = newNode
head1.next = newNode

newNode = Node(30)
head1.next.next= newNode;
head1.next.next.next = None;

countll1 = lenLL(head1)
countll2 = lenLL(head2)

if countll1 > countll2:
    d = countll1 - countll2
    print(intersectionNode(d, head1, head2))
else:
    d = countll2 - countll1
    print(intersectionNode(d, head2, head1))