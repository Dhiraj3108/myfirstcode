stack = []
def pushit():
    ch = 'y'
    while (ch == 'y'):
        inp = input("Enter some character")
        stack.append(inp)
        ch = input("Do you want to enter more values? Enter y/n")
def popit():
    if len(stack) == 0:
        print('Cannot pop from an empty stack!')
    else:
        print('Removed[',stack.pop(),']')
def viewstack():
    print(stack)
pushit()
viewstack()
inp_ch = input("Do you want to pop some value? Enter y/n")
if inp_ch == 'y':
    popit()
    viewstack()
             
