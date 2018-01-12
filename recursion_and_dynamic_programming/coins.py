def coins(n, options=[], output=[]):
    if n < 0:
        return 0
    if n == 0:
        options.sort()
        if options not in output:
            output.append(options)
            return 1
        return 0
    else:
        return coins(n-25, options + [25], output) + coins(n-10, options + [10], output) + coins(n-5, options + [5], output) + coins(n-1, options + [1], output)

def coins_better(n, denoms, index):
    if (index >= len(denoms) - 1):
        return 1
    denom = denoms[index]
    ways = 0

    total = 0
    while total*denom <= n:
        remaining = n - total * denom
        ways +=  coins_better(remaining, denoms, index+1)
        total += 1

    return ways

print(coins(12))
print(coins_better(1000, [25, 10, 5, 1], 0))