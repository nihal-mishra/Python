class Node:
	def __init__(self, data):
		self.next = None
		self.value = data


class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		if self.head:
			last = self.head
			while last.next is not None:
				last = last.next
			last.next = Node(data)
		else:
			self.head = Node(data)

	def print(self):
		temp = self.head
		while temp:
			print(f"{temp.value} ")
			temp = temp.next


if __name__ == '__main__':
	ll = LinkedList()
	ll.insert(10)
	ll.insert(20)
	ll.insert(30)
	ll.print()