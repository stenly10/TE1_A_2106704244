import numpy as np

def generate_sorted_dataset(UB, LB, N, n):
    """ Algoritma untuk generate random sorted dataset
        UB = Upper Bound.
        LB = Lower Bound.
        N = Banyak elemen yang ingin digenerate.
        n = Jumlah baris data pada dataset.
    """
    res = generate_random_dataset(UB, LB, N, n)
    for i in range(len(res)):
        res[i] = sorted(res[i])
    return res

def generate_random_dataset(UB, LB, N, n):
    """ Algoritma untuk generate random dataset.
        UB = Upper Bound.
        LB = Lower Bound.
        N = Banyak elemen yang ingin digenerate.
        n = Jumlah baris data pada dataset.
    """
    res = []
    for i in range(n):
        arr = list(np.random.randint(LB, UB, N))
        res.append(arr)
    return res

def generate_reversed_dataset(UB, LB, N, n):
    """ Algoritma untuk generate random reversed dataset.
        UB = Upper Bound.
        LB = Lower Bound.
        N = Banyak elemen yang ingin digenerate.
        n = Jumlah baris data pada dataset.
    """
    res = generate_random_dataset(UB, LB, N, n)
    for i in range(len(res)):
        res[i] = sorted(res[i], reverse=True)
    return res

def convert_arr(A):
    return " ".join([str(elm) for elm in A])

def generate_random(UB1, UB2, UB3, LB, n):
    SM = 500
    MED = 5000
    BG = 50000
    
    sm = generate_random_dataset(UB1, LB, SM, n)
    med = generate_random_dataset(UB2, LB, MED, n)
    big = generate_random_dataset(UB3, LB, BG, n)
    
    file1 = open("implementasi/dataset/sm_random_dataset.txt", "w")
    file2 = open("implementasi/dataset/med_random_dataset.txt", "w")
    file3 = open("implementasi/dataset/bg_random_dataset.txt", "w")

    for i in range(n):
        sm[i] = convert_arr(sm[i]) + '\n'
        med[i] = convert_arr(med[i]) + '\n'
        big[i] = convert_arr(big[i]) + '\n'
    
    file1.writelines(sm)
    file2.writelines(med)
    file3.writelines(big)

    file1.close()
    file2.close()
    file3.close()

def generate_sorted(UB1, UB2, UB3, LB, n):
    SM = 500
    MED = 5000
    BG = 50000
    
    sm = generate_sorted_dataset(UB1, LB, SM, n)
    med = generate_sorted_dataset(UB2, LB, MED, n)
    big = generate_sorted_dataset(UB3, LB, BG, n)
    
    file1 = open("implementasi/dataset/sm_sorted_dataset.txt", "w")
    file2 = open("implementasi/dataset/med_sorted_dataset.txt", "w")
    file3 = open("implementasi/dataset/bg_sorted_dataset.txt", "w")

    for i in range(n):
        sm[i] = convert_arr(sm[i]) + '\n'
        med[i] = convert_arr(med[i]) + '\n'
        big[i] = convert_arr(big[i]) + '\n'
    
    file1.writelines(sm)
    file2.writelines(med)
    file3.writelines(big)

    file1.close()
    file2.close()
    file3.close()

def generate_reversed(UB1, UB2, UB3, LB, n):
    SM = 500
    MED = 5000
    BG = 50000
    
    sm = generate_reversed_dataset(UB1, LB, SM, n)
    med = generate_reversed_dataset(UB2, LB, MED, n)
    big = generate_reversed_dataset(UB3, LB, BG, n)
    
    file1 = open("implementasi/dataset/sm_reversed_dataset.txt", "w")
    file2 = open("implementasi/dataset/med_reversed_dataset.txt", "w")
    file3 = open("implementasi/dataset/bg_reversed_dataset.txt", "w")

    for i in range(n):
        sm[i] = convert_arr(sm[i]) + '\n'
        med[i] = convert_arr(med[i]) + '\n'
        big[i] = convert_arr(big[i]) + '\n'
    
    file1.writelines(sm)
    file2.writelines(med)
    file3.writelines(big)

    file1.close()
    file2.close()
    file3.close()

if __name__ == "__main__":
    LB = 0
    UB1 = 500
    UB2 = 5000
    UB3 = 50000
    n = 1
    
    generate_random(UB1, UB2, UB3, LB, n)
    generate_sorted(UB1, UB2, UB3, LB, n)
    generate_reversed(UB1, UB2, UB3, LB, n)