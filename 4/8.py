def reverse_number(signed_num):
    if(signed_num == 0):
        return 0
    num = abs(signed_num)
    rnum = num % 10
    num //= 10
    while num != 0:
        rnum = rnum*10 + num % 10
        num //= 10
    return rnum * (signed_num // abs(signed_num))


def reverse_number_v2(signed_num):

    num = abs(signed_num)
    rnum = num % 10
    num //= 10
    while num != 0:
        rnum = rnum*10 + num % 10
        num //= 10
    return rnum if signed_num < 0 else -rnum


print(reverse_number_v2(145))
