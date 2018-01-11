
def insertion(n, m, i, j):
    n_len = int.bit_length(n)
    m_len = int.bit_length(m)

    # clear bits 2-6
    for x in range(i, j+1): 
        n = n & ~(1 << x)

    shift_amount = j-m_len+1

    shifted_m = m << shift_amount

    return (n | shifted_m)

print(insertion(0b10000111100, 0b10011, 2, 6))