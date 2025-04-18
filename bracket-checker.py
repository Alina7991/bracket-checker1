class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def is_balanced_brackets(s):
    stack = Stack()
    brackets = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in brackets:
            stack.push(char)
        elif char in brackets.values():
            top = stack.pop()
            if top is None or brackets[top] != char:
                return False
    return stack.is_empty()

examples = ["([]{})", "([)]", "{[}", "()"]
for example in examples:
    result = is_balanced_brackets(example)
    print(f"{example}:{"Правильная скобочная последовательность" if result else "Неправильная скобочная последовательность"}")
