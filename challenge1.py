def sum_trace(array):
    trace = 0

    for irow, row in enumerate(array):
        for icolumn, column in enumerate(row):
            if irow == icolumn:
                trace += column

    return trace


def has_repeated(row):
    return len(set(row)) != len(row)


def num_repeated_rows(array):
    return sum(has_repeated(row) for row in array)


def num_repeated_columns(array):
    [(0, 0), (1, 0), (2, 0)]

    size = range(len(array))

    total = 0

    for i in size:
        items = [array[j][i] for j in size]

        if len(set(items)) != len(items):
            total += 1

    return total


def vestigium():
    cases = int(input())

    for i in range(cases):
        array = []

        size = int(input())

        for _ in range(size):
            row = input()
            array.append([int(x) for x in row.split()])

        trace = sum_trace(array)
        rows = num_repeated_rows(array)
        columns = num_repeated_columns(array)

        print('Case #{}: {} {} {}'.format(i + 1, trace, rows, columns))


vestigium()
