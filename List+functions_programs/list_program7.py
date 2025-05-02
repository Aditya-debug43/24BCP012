stack = []
while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    ch = int(input())
    if ch == 1:
        stack.append(input())
    elif ch == 2:
        if stack: print(stack.pop())
    elif ch == 3:
        print(stack)
    else:
        break