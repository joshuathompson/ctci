
def number_of_ones_in_binary(dec):
    num_bits = int.bit_length(dec)
    number_of_one_bits = 0

    for x in range(num_bits):
        bit = ((dec & (1 << x)) != 0)
        if bit:
            number_of_one_bits += 1

    return number_of_one_bits

def find_similar_numbers(num):
    num_bits_original = number_of_ones_in_binary(num)

    searching = True
    count = 1
    while searching:
        number_to_check = num + count
        num_bits_new = number_of_ones_in_binary(number_to_check)

        if num_bits_original == num_bits_new:
            print("Found higher number: " + str(number_to_check))
            searching = False

        count += 1

    searching = True
    count = 1
    while searching:
        number_to_check = num - count
        num_bits_new = number_of_ones_in_binary(number_to_check)

        if num_bits_original == num_bits_new:
            print("Found lower number: " + str(number_to_check))
            searching = False

        count += 1

find_similar_numbers(8)