import time
import bidirectional_conditional_insertion_sort as bcis
import counting_sort as cs
import numpy as np

def get_time_bcis(arr):
    arr2 = [x for x in arr]
    start = time.time()
    bcis.bidirectional_conditional_insertion_sort(arr2)
    end = time.time()
    return arr2, (end-start) * 1000

def get_time_cs(arr):
    arr2 = [x for x in arr]
    start = time.time()
    res = cs.counting_sort(arr2)
    end = time.time()
    return res, (end-start) * 1000

def get_time_each_algorithm(arr):
    exc_time_bcis = []
    exc_time_cs = []
    for elm in arr:
        elm = elm.strip().split()
        elm = [int(x) for x in elm]
        a, b = get_time_bcis(elm)
        c, d = get_time_cs(elm)
        exc_time_bcis.append(b)
        exc_time_cs.append(d)
    print("bcis:", np.mean(exc_time_bcis))
    print("cs:", np.mean(exc_time_cs))

def compare_sm():
    print("========= SMALL SORTED DATASET =========")
    file1 = open("implementasi/dataset/sm_sorted_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= MEDIUM SORTED DATASET =========")
    file1 = open("implementasi/dataset/med_sorted_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= BIG SORTED DATASET =========")
    file1 = open("implementasi/dataset/bg_sorted_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= SMALL RANDOM DATASET =========")
    file1 = open("implementasi/dataset/sm_random_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= MEDIUM RANDOM DATASET =========")
    file1 = open("implementasi/dataset/med_random_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= BIG RANDOM DATASET =========")
    file1 = open("implementasi/dataset/bg_random_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= SMALL REVERSED DATASET =========")
    file1 = open("implementasi/dataset/sm_reversed_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= MEDIUM REVERSED DATASET =========")
    file1 = open("implementasi/dataset/med_reversed_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")

    print("========= BIG REVERSED DATASET =========")
    file1 = open("implementasi/dataset/bg_reversed_dataset.txt", "r")
    arr = file1.readlines()
    file1.close()
    get_time_each_algorithm(arr)
    print("=======================================\n")
    
    
def main():
    compare_sm()

if __name__ == "__main__":
    main()