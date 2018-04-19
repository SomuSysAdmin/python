def process_command(cmd, lst):
    cl = cmd.split(' ')
    if len(cl) == 3:
        (act, op1, op2) = tuple(cl)
    elif len(cl) == 2:
        (act, op1) = tuple(cl)
    elif len(cl) == 1:
        act = cl[0]

    # Executing the command
    if act == 'insert':
        lst.insert(int(op1), int(op2))
    elif act == 'print' :
        print(lst),
    elif act == 'remove':
        lst.remove(int(op1)),
    elif act == 'append':
        lst.append(int(op1)),
    elif act == 'sort':
        lst.sort(),
    elif act == 'pop':
        lst.pop(),
    elif act == 'reverse':
        lst.reverse()
    else:
        print("RETRY!")


if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(0, N):
        line = []
        line = input()
        process_command(line, lst)
