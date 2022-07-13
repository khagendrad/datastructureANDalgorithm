# Implementation of stack

#creating stack
def create_stack():
    stack = []
    return stack 

# checking stack empty or not  
def check_empty(stack):
    return len(stack)==0

# adding items 
def push(stack, item):
    stack.append(item)
    print("Pushed item"+ item)

# removing an element from the stack 
def pop(stack):
    if check_empty(stack):
        return 'stack is empty'
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, 'kd')
push(stack, 'mo')
print('poped item:'+ pop(stack))
print(stack.pop())