class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def delete_max(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return max_value

    def heapify_down(self, index):
        n = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = \
                    self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def display(self):
        print(self.heap)


# Example
h = MaxHeap()

h.insert(50)
h.insert(30)
h.insert(40)
h.insert(10)
h.insert(20)
h.insert(60)

h.display()

print("Deleted:", h.delete_max())
h.display()
