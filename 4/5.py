def flip_bits(i):
    result = 0
    while i != 1:
        result |= (i & 0x1)
        i >>= 1
        result <<= 1
    return result >> 1


def add_no_plus(a, b):
    carry = 0
    result = 2
    while a != 0 or b != 0:
        a_bit = a & 0x1
        b_bit = b & 0x1
        current_bit = a_bit ^ b_bit ^ carry
        carry = ((a_bit | b_bit) & carry) | (a_bit & b_bit)
        result |= current_bit
        b >>= 1
        a >>= 1
        result <<= 1
    result |= carry
    return flip_bits(result)


print(add_no_plus(8, 7))
