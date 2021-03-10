class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next


def countPairs(llist1, llist2):
    X = int(input("Enter a value to CountPair the lists to: "))
    current1 = llist1.head
    current2 = llist2.head
    count = 0
    while (current1 and current2):
        if current1.data + current2.data == X:
            count += 1
        current1 = current1.next
        current2 = current2.next

    if current1 is None and current2 is None:
        print(f"The total is: {count}")
        return True
print("Welvome to the Count Pairs program, the input should be as following #Input: 1 2 3 4 5")
llist1 = LinkedList()
llist2 = LinkedList()

data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))

data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))

countPairs(llist1, llist2)

