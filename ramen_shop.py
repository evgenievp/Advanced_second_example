from collections import  deque as dq

bows = [int(x) for x in input().split(", ")]
customers = dq([int(x) for x in input().split(", ")])

while bows and customers:
    bowl = bows[-1]
    customer = customers[0]
    if bowl == customer:
        customers.popleft()
        bows.pop()
        continue
    elif bowl < customer:
        customers[0] -= bowl
        bows.pop()
    elif bowl > customer:
        bows[-1] -= customer
        customers.popleft()

if not customers:
    print(f"Great job! You served all the customers.")
    if bows:
        bowls = [str(x) for x in bows]
        print(f"Bowls of ramen left: {', '.join(bowls)}")
elif not bows:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    customs = [str(x) for x in customers]
    print(f"Customers left: {', '.join(customs)}")
