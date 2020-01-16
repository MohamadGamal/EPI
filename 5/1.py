def dutch_flag(A, p):
    pivot = A[p]
    lt_size = bt_size = p_size = 0
    for i in A:
        if i < pivot:
            lt_size += 1
        elif i > pivot:
            bt_size += 1
        else:
            p_size += 1
    lt_ptr = 0
    bt_ptr = len(A)-1
    p_ptr = lt_size
    while lt_ptr < lt_size:
        curr_elem = A[lt_ptr]
        if curr_elem > pivot:
            A[lt_ptr], A[bt_ptr] = A[bt_ptr], A[lt_ptr]
            bt_ptr -= 1
        elif curr_elem == pivot:
            A[lt_ptr], A[p_ptr] = A[p_ptr], A[lt_ptr]
            p_ptr += 1
        else:
            lt_ptr += 1
    while p_ptr < lt_size+p_size:
        curr_elem = A[p_ptr]
        if curr_elem > pivot:
            A[bt_ptr], A[p_ptr] = A[p_ptr], A[bt_ptr]
            bt_ptr += 1
        else:
            p_ptr += 1
    return A


def swap_in_arr(A, index_a, index_b):
    if(index_a > 0 and index_b > 0 and index_a != index_b):
        A[index_a], A[index_b] = A[index_b], A[index_a]


def dutch_flag_v2(A, pivot_index):
    pivot = A[pivot_index]
    next_smaller, next_equal, next_bigger = 0, 0, len(A) -1 
    while next_bigger >= next_equal:
        element = A[next_equal]
        if element > pivot:
            A[next_bigger], A[next_equal] = A[next_equal], A[next_bigger]
            next_bigger -= 1
        elif element < pivot:
            A[next_equal], A[next_smaller] = A[next_smaller], A[next_equal]
            next_smaller += 1
            next_equal += 1
        else:
            next_equal += 1
    return A


print(dutch_flag_v2([0, 1, 2, 2, 1,3,3,3,3,2,1, 1], 5))
