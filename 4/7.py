def inhouse_pow_v1(num, pow):
    if pow == 0:
        return 1
    sqrt_pow = inhouse_pow_v1(num, pow//2)
    power = sqrt_pow * sqrt_pow
    if pow % 2 != 0:
        power *= num
    return power


print(inhouse_pow_v1(3, 80), 3**80)
