class CustomRange:
    def __init__(self, start, end):
        self.i = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            current = self.i
            self.i += 1
            return current
        else:
            raise StopIteration()


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)


new_one_to_eight = CustomRange(1, 8)
for num in new_one_to_eight:
    print(num)