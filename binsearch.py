def binsearch(list, x):
    i = 0
    j = len(list) - 1 
    m = int(j / 2)
    while list[m] != x and i < j:
        if x > list[m]:
            i = m + 1
        else:
            j = m - 1
        m = int((i + j)/2)
    if i > j:
        return 'Нет такого'
    else:
        return m

