def divide(lst, n):
    # break the input down to multiple subsets to be run on multiple processes
    l = len(lst)
    assert n <= l

    individual = l // n
    divided = []
    it = iter(lst)
    i, j = 0, 0

    while j < n:
        part = []
        for _ in range(individual):
            part.append(next(it))
            i += 1
        divided.append(part)
        j += 1

    while i < l:
        for j in range(len(divided)):
            divided[j].append(next(it))
            i += 1
            if i >= l:
                break
    return divided

