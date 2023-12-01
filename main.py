class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: object) -> object:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def parenthesis_balanced(data):
    s = Stack()
    open = ['(', '[', '{']
    close = [')', ']', '}']
    for i in data:
        balance = False
        if i not in open and i not in close: continue
        # elif i == '(' or i == '[' or i == '{': s.push(i)
        elif i in open: s.push(i)
        # elif (i == ')' or i == ']' or i == '}') and (s.is_empty() is False):
        elif i in close and (s.is_empty() is False):
            if (i == ')' and s.peek() == '(') or (i == ']' and s.peek() == '[') or (i == '}' and s.peek() == '{'):
                s.pop()
                if s.is_empty(): balance = True
            else: break
        else: break
    if balance:
        print(f' {data} - скобки сбалансированы')
    else: print(f' {data} - скобки не сбалансированы')

parenthesis_balanced('[([])((([[[]]])))]{()}')
parenthesis_balanced('{{[(])]}}')
parenthesis_balanced("[('l', 'p'), [1]], {}, [1:'t', 2:'r']")
parenthesis_balanced('}{[(])]}}')
parenthesis_balanced('{{[')
