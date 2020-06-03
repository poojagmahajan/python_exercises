

### logic --- push all input)string characters in stack...then pop them from stack as a reverse string


from stack import Stack
def reverse_string(stack, input_str):
  for i in range(len(input_str)):       ## push string on a stack
    stack.push(input_str[i])
  rev_str = ""                          ## create empty string
  while not stack.is_empty():           # till stack is not empty
    rev_str += stack.pop()             ## pop all characters from stack and store it in rev_str

  return rev_str              

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))

