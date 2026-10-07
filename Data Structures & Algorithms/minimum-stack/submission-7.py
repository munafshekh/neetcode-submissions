class MinStack:
    def __init__(self):
        self.stack = []
        self.curr_min = float("inf")
        self.minstack = []

    def push(self, val: int) -> None:
        if val <= self.curr_min:
            self.curr_min = val
            self.minstack.append(self.curr_min)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            #checking if the last val in stack was curr_min
            if self.stack[-1] == self.curr_min:
                if self.minstack:
                    # [-1,0,3,-2,3]
                    del self.minstack[-1]
                    if self.minstack:
                        self.curr_min = self.minstack[-1]
                    else:
                        self.curr_min = float('inf')
            del self.stack[-1]
            #[4, -4, ]
            #[]
            #

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min
