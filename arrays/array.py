import ctypes

class Array(object):
    def __init__(self):
        self.item_count = 0
        self.array_capacity = 1
        self.primary_array = self._create_array(self.array_capacity)

    def _create_array(self, array_capacity):
        return (array_capacity * ctypes.py_object)()

    def list(self):
        for items in self.primary_array:
            return " ".join(str(self.primary_array[x]) for x in range(self.item_count))

    def __len__(self):
        return self.item_count

    def __getitem__(self, item_index):
        if not 0 <= item_index < self.item_count:
            return IndexError('Index out of range!')
        return self.primary_array[item_index]


x = Array()
print('x')
