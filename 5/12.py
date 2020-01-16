from random import randint


def random_uniform_k_subset(A, k):
    for i in range(0, k):
        choice = randint(i, k)
        A[i], A[choice] = A[choice], A[i]
    return A[0: k]


print(random_uniform_k_subset([2, 3, 4, 6, 2, 5, 7, 8, 1, 12, 45], 5))
