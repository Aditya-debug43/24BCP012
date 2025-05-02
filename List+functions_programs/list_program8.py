from collections import deque
q = deque()
while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = int(input())
    if ch == 1:
        q.append(input())
    elif ch == 2:
        if q: print(q.popleft())
    elif ch == 3:
        print(q)
    else:
        break