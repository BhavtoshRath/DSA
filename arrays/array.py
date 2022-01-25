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
            self.arrayItems = [item] + self.arrayItems[1:]
        elif position == len(self.arrayItems) - 1:
            self.arrayItems = self.arrayItems[:-1] + [item]
        elif position >= len(self.arrayItems):
            return IndexError('position out of bound!')
        else:
            arr_left = self.arrayItems[:position]
            arr_right = self.arrayItems[position+1:]
            arr_left.append(item)
            self.arrayItems = arr_left + arr_right

    def delete(self, item):  # Assuming single occurrence. and replace deleted item with 0.
        flag = 0
        for i in self.arrayItems:
            if self.arrayItems[i] == item:
                flag = 1
                self.arrayItems[i] = 0
        if flag == 0:
            print('Item not in array')


if __name__ == '__main__':
    a = Array(10, int)
    a.insert(9, 9)
    a.insert(0, 0)
    a.insert(4, 4)
    a.insert(7, 7)
    a.delete(4)
    print(a)
    a.delete(7)
    print(a)
