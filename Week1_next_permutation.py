def next_permutation(A):
    inverse_point = len(A) - 2

    while inverse_point >= 0 and A[inverse_point] >= A[inverse_point + 1]:
        inverse_point -= 1

    if inverse_point < 0:
        return []

    for i in reversed(range(inverse_point, len(A))):
        if A[i] > A[inverse_point]:
            A[i], A[inverse_point] = A[inverse_point], A[i]
            break

    A[inverse_point + 1:] = reversed(A[inverse_point + 1:])
    return A

