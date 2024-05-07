import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]

        #print('key', key)

        j = i-1

        #print('lst[j]', lst[j])

        while j >=0 and key < lst[j] :
                #print('before', lst)
                lst[j+1] = lst[j]
                #print('after', lst)
                j -= 1
                #print('lst[j]', lst[j])

        lst[j+1] = key
        #print(' ', lst)
        #print('---\n')
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    #print('p1 a', arr)

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #print('p1 lr', left_half, right_half)

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    #print('p2 lr', left, right)

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        #print('p2 m', merged)

    # Якщо в лівій або правій половині залишилися елементи,
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
        #print('p2 la', merged)

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
        #print('p2 ra', merged)

    return merged

numbers = random.sample(range(1, 1000000), 500)

print("Calculation of time used by insertion sort")
print(timeit.timeit(lambda: insertion_sort(numbers.copy()), number=20))

print("Calculation of time used by merge sort")
print(timeit.timeit(lambda: merge_sort(numbers.copy()), number=20))

print("Calculation of time used by timsort")
print(timeit.timeit(lambda: sorted(numbers.copy()), number=20))

#Results are next 

#Calculation of time used by insertion sort - 0.11789710000448395
#Calculation of time used by merge sort - 0.019358200006536208
#Calculation of time used by timsort- 0.0010315999970771372

#as a conclusion 

#timsort is 10x faster then merge sort
#timsort is 100x faster then insertion sort
