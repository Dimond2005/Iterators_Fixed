from pprint import pprint

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None], [56, 4, 'Over']
]


class FlatIterator:
    def __init__(self, input_list):
        self.input_list = input_list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        # for self.vale in self.input_list[self.cursor]:
        #     return self.vale
        if self.cursor == len(self.input_list):
            raise StopIteration
        return self.input_list[self.cursor]


# for item in FlatIterator(nested_list):
#     print(item)
    # for element in item:
    #     print(element)
# #
# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)


def generator(imput_list):
    for value in imput_list:
        for element in value:
            yield element

print()
for element in generator(nested_list):
    print(f'Сгенерировано ', element)
