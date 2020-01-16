from math import ceil


def spiral_order_util(A, order, skip):
    end = len(A)-skip - 1
    if skip == end:
        order.append(A[skip][end])
    for i in range(skip, end):
        order.append(A[skip][i])
    for i in range(skip, end):
        order.append(A[i][end])
    for i in range(end, skip, -1):
        order.append(A[end][i])
    for i in range(end, skip, -1):
        order.append(A[i][skip])


def spiral_order(A):
    order = []
    for i in range(0, ceil(len(A)/2)):
        spiral_order_util(A, order, i)
    return order


print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8],
                    [9, 10, 11, 12], [13, 14, 15, 16]]))
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_order([[1]]))
