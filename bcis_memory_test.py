from memory_profiler import memory_usage
import bidirectional_conditional_insertion_sort as bcis
import numpy as np
import tracemalloc
def sm_sorted():
    file1 = open("implementasi/dataset/sm_sorted_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def med_sorted():
    file1 = open("implementasi/dataset/med_sorted_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def bg_sorted():
    file1 = open("implementasi/dataset/bg_sorted_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def sm_random():
    file1 = open("implementasi/dataset/sm_random_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def med_random():
    file1 = open("implementasi/dataset/med_random_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def bg_random():
    file1 = open("implementasi/dataset/bg_random_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def sm_reversed():
    file1 = open("implementasi/dataset/sm_reversed_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def med_reversed():
    file1 = open("implementasi/dataset/med_reversed_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def bg_reversed():
    file1 = open("implementasi/dataset/bg_reversed_dataset.txt", "r")
    arr = file1.readlines()
    arr_memory = []
    for i in range(len(arr)):
        arr[i] = arr[i].strip().split()
        arr[i] = [int(x) for x in arr[i]]
        tracemalloc.start()
        bcis.bidirectional_conditional_insertion_sort(arr[i])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        arr_memory.append(peak/ pow(10,6))
    return np.mean(arr_memory)

def main():
    print("========== BCIS ==========")
    print("small sorted:", sm_sorted(), "MB")
    print("medium sorted:", med_sorted(), "MB")
    print("big sorted:", bg_sorted(), "MB")
    print("--------------------------")
    print("small random:", sm_random(), "MB")
    print("medium random:", med_random(), "MB")
    print("big random:", bg_random(), "MB")
    print("--------------------------")
    print("small reversed:", sm_reversed(), "MB")
    print("medium reversed:", med_reversed(), "MB")
    print("big reversed:", bg_reversed(), "MB")

if __name__ == "__main__":
    main()