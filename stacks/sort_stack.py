unorderedStack = [5, 4, 6, 4, 3, 12, 23, 10, 5, 10, 3, 12]
orderedStack = []

pop = None
hold = None

while len(unorderedStack) > 0:
    pop = unorderedStack.pop()

    if hold is None:
        hold = pop
    elif pop >= hold:
        for item in reversed(orderedStack):
            if pop > item:
                moveBack = orderedStack.pop()
                unorderedStack.append(moveBack)

        orderedStack.append(pop)
    else:
        orderedStack.append(hold)
        hold = pop

if hold is not None:
    orderedStack.append(hold)

print(orderedStack)