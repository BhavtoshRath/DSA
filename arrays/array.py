import ctypes


class Array(object):

    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems = [arrayType(0)] * sizeOfArray
        self.arrayType = arrayType

    def __str__(self):  # https://stackoverflow.com/questions/41168899/does-python-str-function-call-str-function-of-a-class
        return "".join(str(i) for i in self.arrayItems)

    def __len__(self):
        return len(self.arrayItems)

    def __setitem__(self, index, item):
        self.arrayItems[index] = item

    def __getitem__(self, index):
        return self.arrayItems[index]

    def search(self, item):
        for i in self.arrayItems:
            if i == item:
                return True
        return False

    def insert(self, item, position): # Insert can be either at a position or at the end
        if position == 0:
            return [item].append(self.arrayItems)
        elif position == len(self.arrayItems) - 1:
            return self.arrayItems.append([item])
        elif position >= len(self.arrayItems):
            return IndexError('position out of bound!')
        else:
            arr_left = self.arrayItems[:position]
            arr_right = self.arrayItems[position:]
            temp1 = arr_left.append([item])
            self.arrayItems = temp1.append(arr_right)
            return self.arrayItems




a = Array(10, str)
x = a[4]
print('x')
