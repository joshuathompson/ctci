def flip_bit_to_win(num):
    num_bits = int.bit_length(num)
    bits = []

    for x in range(num_bits):
        bit = ((num & (1 << x)) != 0)
        bits.insert(0, int(bit))

    longest_string = 0
    for index, bit in enumerate(bits):
        original_bit = bits[index]
        bits[index] = 1

        count = 0
        for sbit in bits:
            if sbit == 1:
                count += 1
            else:
                if count > longest_string:
                    longest_string = count

                count = 0

        if count > longest_string:
            longest_string = count

        bits[index] = original_bit

    return longest_string

print(flip_bit_to_win(5))
print(flip_bit_to_win(8))
print(flip_bit_to_win(11))
print(flip_bit_to_win(0b1110110011101))