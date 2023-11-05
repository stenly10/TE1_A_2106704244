import math
import counting_sort as cs
def bidirectional_conditional_insertion_sort(A):
    """Algoritma bcis dengan array A dimulai dari indeks 0.
        Referensi: Adnan Saher Mohammed, S¸ahin Emrah Amrahov, and Fatih V C¸ elebi. Bidirectional Conditional
        Insertion Sort algorithm; An efficient progress on the classical insertion sort. Future Generation
        Computer Systems, 71:102–112, 2017.
    """
    LEFT = 0
    RIGHT = len(A)-1
    SL = LEFT
    SR = RIGHT
    while SL < SR:
        A[SR], A[math.floor(SL+(SR-SL)/2)] = A[math.floor(SL+(SR-SL)/2)], A[SR]
        if A[SL] == A[SR]:
            if is_equal(A, SL, SR) == -1:
                return
        if A[SL] > A[SR]:
            A[SL], A[SR] = A[SR], A[SL]
        
        if SR-SL >= 100:
            for i in range(SL+1, math.floor(math.pow(SR-SL, 0.5))+1):
                if A[SR] < A[i]:
                    A[SR], A[i] = A[i], A[SR]
                elif A[SL] > A[i]:
                    A[SL], A[i] = A[i], A[SL]
        i = SL + 1
        LC = A[SL]
        RC = A[SR]
        while i<SR:
            curr = A[i]
            if curr >= RC:
                A[i] = A[SR-1]
                ins_right(A, curr, SR, RIGHT)
                SR = SR-1
            elif curr <= LC:
                A[i] = A[SL+1]
                ins_left(A, curr, SL, LEFT)
                SL = SL+1
                i += 1
            else:
                i += 1
        
        SL = SL+1
        SR = SR-1

def is_equal(A, SL, SR):
    for k in range(SL+1, SR):
        if A[k] != A[SL]:
            A[k], A[SL] = A[SL], A[k]
            return k
    return -1

def ins_right(A, curr, SR, RIGHT):
    j = SR
    while j<=RIGHT and curr > A[j]:
        A[j-1] = A[j]
        j += 1
    A[j-1] = curr

def ins_left(A, curr, SL, LEFT):
    j = SL
    while j>=LEFT and curr<A[j]:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = curr

if __name__ == "__main__":
    file1 = open("implementasi/dataset/bg_random_dataset.txt", "r")
    arr = file1.readline().strip().split()
    arr = [int(x) for x in arr]
    arr2 = []
    for elm in arr:
        arr2.append(elm)
    bidirectional_conditional_insertion_sort(arr)
    arr2.sort()
    print(arr == arr2)

