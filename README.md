### Программа, которая проверяет, является ли строка правильной скобочной последовательностью.

Правильной скобочной последовательностью считается последовательность, в которой каждая открывающая скобка (например, '(', '{', '[') имеет соответствующую закрывающую скобку (')', '}', ']'). При этом скобки должны быть правильно вложены друг в друга, и порядок их следования должен быть корректным.

#### Программа проверяет, является ли введённая строка правильной скобочной последовательностью — то есть:
- Все открывающие скобки имеют закрывающие
- Скобки правильно вложены
- Поддерживаются типы скобок: (), {}, [] 

Примеры:
- **Правильная** скобочная последовательность: "([]{})"
- **Неправильная** скобочная последовательность: "([)]"
- **Неправильная** скобочная последовательность: "{[}"
- **Правильная** скобочная последовательность: "()"

### Используется структура данных Стек

class Stack:
- def push(self, ...)
- def pop(self, ...)
- def peek(self, ...)
- def is_empty(self, ...)

И основная функция:

```
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
```


Результатом выполнения программы будет сообщение о том, является ли данная строка правильной скобочной последовательностью или нет. 
````
for example in examples:
    result = is_balanced_brackets(example)
    print(f"{example}:{"Правильная скобочная последовательность" if result else "Неправильная скобочная последовательность"}")
````