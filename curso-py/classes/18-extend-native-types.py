class List(list):
    def prepend(self, item):
        self.insert(0, item)


list = List([1, 2, 3])
list.append(4)
list.prepend(0)
print(list)
