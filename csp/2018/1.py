my_2d_list = [
    [3, 1],
    [1, 5],
    [4, 2],
    [1, 3],
    [5, 4],
    [9, 8],
    [2, 7],
    [6, 6]
]

sorted_list = sorted(my_2d_list, key=lambda x: x[1] ** 2)
print(sorted_list)
