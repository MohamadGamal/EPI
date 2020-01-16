def inc_num(n):
    n.reverse()
    carry = 1
    for d_ind in range(0, len(n)):
        carry_sum = carry + n[d_ind]
        n[d_ind], carry = carry_sum % 10, carry_sum//10
    if carry == 1:
        n.append(1)
    n.reverse()
    return n


print(inc_num([9, 9, 9]))
