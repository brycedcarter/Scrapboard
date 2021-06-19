#! /usr/bin/python3
"""
Practicing writing some sorting algos
"""
# import random
import time

lst = [5, 7, 3, 4, 8, 9, 2]


def quicksort(lst: list, s, e):
    if len(lst[s:e]) <= 1:
        return lst
    pi = len(lst)//2
    p = lst[pi]
    i = s
    j = e-1

    print(f'piviot: {p}')
    while i < j:
        print(lst[s:e])
        print(f'i={lst[i]}({i}), j={lst[j]}({j})')
        if lst[i] <= p:
            i += 1
            continue
        if lst[j] >= p:
            j -= 1
            continue
        t = lst[j]
        lst[j] = lst[i]
        lst[i] = t
        i += 1
        j -= 1
    print(i, j)
    print(f'FINAL: {lst[s:e]}')
    if lst[i] > p:
        t = lst[i]
        lst[i] = lst[pi]
        lst[pi] = t
        pi = i
    elif lst[j] < p:
        t = lst[j]
        lst[j] = lst[pi]
        lst[pi] = t
        pi = j
    print(f'FINAL: {lst[s:e]}')

    if len(lst[s:e]) <= 2:
        return lst
    quicksort(lst, s, pi-1)
    quicksort(lst, pi+1, e)

    print(lst)
    return lst


def mergesort(lst: list, s: int, e: int) -> list:
    if len(lst) == 1:
        return lst
    else:
        splitpoint = len(lst)//2
        l1 = mergesort(lst[:splitpoint])
        l2 = mergesort(lst[splitpoint:])

    i = 0
    j = 0
    r = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            r.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            r.append(l2[j])
            j += 1
    if i == len(l1):
        r += l2[j:]
    else:
        r += l1[i:]
    return r


def best_stock_price(lst: list):
    best_dates = (0, 0)
    best_profit = 0
    lowest_date = 0
    lowest_price = lst[lowest_date]

    for current_date, current_price in enumerate(lst):
        if current_price < lowest_price:
            lowest_price = current_price
            lowest_date = current_date

        if (current_price - lowest_price) > best_profit:
            best_profit = current_price - lowest_price
            best_dates = (lowest_date, current_date)

    return best_dates


def countingsort(lst: list, radix: int = None, rng: int = 10):
    c = [0] * (rng+1)  # counting array
    o = [0] * len(lst)  # output array
    # counter number of time each eleent is seen
    for e in lst:
        if radix is not None:
            c[(e//radix) % rng]
        else:
            c[e] += 1

    # extablish starting location for each value
    v = -1
    for i in range(len(c)):
        v += c[i]
        c[i] = v

    # fill the output array based on the positions from the value array
    i = len(lst)-1
    while i >= 0:
        v = lst[i]
        if radix is not None:
            k = v//(radix) % rng
        else:
            k = v
        o[c[k]] = v
        c[k] -= 1
        i -= 1

    return o


def radixsort(lst: list):
    m = max(lst)
    r = 10 ** 0
    while m//r > 1:
        lst = countingsort(lst, r)
        r *= 10
    return lst


def heapsort(lst: list):
    pass


if __name__ == "__main__":
    # quicksort(lst, 0, len(lst))
    # mergesort(lst)
    lst = [0, 1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 6, 10000000,
           7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]

    print('====== COUNTING SORT ======')
    s = time.time()
    print(countingsort(list(lst), rng=max(lst)))
    print(time.time()-s)

    print('======= RADIX SORT =======')
    s = time.time()
    print(radixsort(list(lst)))
    print(time.time()-s)

    print('====== QUICK SORT ======')
    s = time.time()
    # print(quicksort(list(lst), 0, len(lst)))
    print(time.time()-s)
