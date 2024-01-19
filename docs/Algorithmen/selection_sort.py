def selection_sort(a):
    for j in range(len(a) - 1):
        key = a[j]
        index = j
        for i in range(j + 1, len(a)):
            if a[i] < a[index]:
                index = i
        a[j] = a[index]
        a[index] = key
    return a

to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print('Unsortiert:', to_sort)
print('Sortiert:  ', selection_sort(to_sort))