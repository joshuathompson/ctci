import math

def get_bits(dec):
    num_bits = int.bit_length(dec)
    bits = []

    for x in range(num_bits):
        bit = ((dec & (1 << x)) != 0)
        bits.insert(0, int(bit))

    return bits

def conversion(a, b):
    a_bits = get_bits(a)
    b_bits = get_bits(b)

    conversions_required = 0
    times_to_loop = 0

    len_a = len(a_bits)
    len_b = len(b_bits)

    if len_a == len_b:
        times_to_loop = len_a
    elif len_a > len_b:
        times_to_loop = len_b
        conversions_required = len_a - len_b
    else:
        times_to_loop = len_a
        conversions_required = len_b - len_a

    for i in range(times_to_loop):
        a_bit = a_bits[times_to_loop-i-1]
        b_bit = b_bits[times_to_loop-i-1]

        if a_bit != b_bit:
            conversions_required += 1

    print(conversions_required)

conversion(44, 15)