# num = [1,2,3]

# iter_num = iter(num)
# print(next(iter_num))
# print(next(iter_num))
# print(next(iter_num))


# def our_own_for_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break
# a = [1,2,3,4,5]
# b = (1,2,3,4,5)
# c = {1,2,3,4,5}
# d = {1:2,2:3}

# our_own_for_loop()

class My_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return IteratorRang(self)


class IteratorRang:
    def __init__(self, iterable_object):
        self.iterable = iterable_object
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        else:
            current = self.iterable.start
            self.iterable.start +=1
            return current

