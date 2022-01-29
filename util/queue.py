class Queue:
    def __init__(self):
        self.buffer = []
        self.current_length = 0

    def insert(self, item):
        self.current_length += 1
        self.buffer.append(item)

    def delete(self):
        self.current_length -= 1
        return self.buffer.pop(0)

    def is_empty(self):
        return self.current_length == 0

    