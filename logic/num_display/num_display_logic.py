from utils.state.state import State
 
class NumDisplayLogic:
    def __init__(self, num: State[str]) -> None:
        self.num = num

    def increment(self):
        self.num.set(str(int(self.num.get()) + 1))

    def decrement(self):
        self.num.set(str(int(self.num.get()) - 1))