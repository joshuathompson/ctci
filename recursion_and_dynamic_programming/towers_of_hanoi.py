stack_one = [8, 7, 6, 'five', 4, 3, 2, 1]
stack_two = []
stack_three = []

total_to_move = len(stack_one)

for i in range(total_to_move):
    new_total = total_to_move-i-1
    for j in range(new_total):
        x = stack_one.pop()
        stack_two.insert(0, x)

    stack_three.append(stack_one.pop())
    
    stack_one = stack_two
    stack_two = []

print(stack_one)
print(stack_two)
print(stack_three)