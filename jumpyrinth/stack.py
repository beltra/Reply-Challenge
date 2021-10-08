class Stack:
    def __init__(self, stack = []) -> None:
        self.__stack = stack
    def __str__(self) -> str:
        return str(self.__stack)
    def push(self, arg) -> None:
        self.__stack.append(arg)
    def pop(self):
        return self.__stack.pop()
    def empty(self) -> None:
        self.__stack = []
