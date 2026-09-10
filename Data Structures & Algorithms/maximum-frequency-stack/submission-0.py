class FreqStack:
    def __init__(self):
        self.counts = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        freq = self.counts[val]
        
        self.stacks[freq].append(val)
        self.max_count = max(freq, self.max_count)

    def pop(self) -> int:
        val = self.stacks[self.max_count].pop()
        
        self.counts[val] -= 1

        if not self.stacks[self.max_count]:
            self.max_count -= 1
            
        return val
