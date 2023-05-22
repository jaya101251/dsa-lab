operators=set(['+','-','*','/','(',')','^'])
priority={'+': 1,'-':1,'*':2,'/':3,'^':3}

def infix_to_postfix(Expression):
    stack=[]
    output=''
    for character in expression:
        if character not in operators:
            output += character
        elif character == '(':
            stack.append('(')
        elif character == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[character] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(character)
    while stack:
        output += stack.pop()
    return output

expression = input("enter infix expression:")
print("infix notation:", expression)
print("postfix notation:", infix_to_postfix(expression))
