def counting_sort(A):
    """ Algoritma counting sort dengan array A dimulai dari indeks 0 """
    C = []
    B = [0] * len(A)
    n = len(A)
    k = max(A)
    for i in range(k+1):
        C.append(0)

    for j in range(n):
        C[A[j]] += 1

    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
        
    for j in range(n-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B