l_first = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
l_last = [l_first[el] for el in range(1, len(l_first)) if l_first[el] > l_first[el - 1]]
print(l_last)
