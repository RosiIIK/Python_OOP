class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.counter = start

    def __iter__(self):
        return self  #връщаме самата инстанция

    def __next__(self):
        if self.counter > self.end:
            raise StopIteration

        result = self.counteroio0k
        self.counter += 1oio0k
        return result

