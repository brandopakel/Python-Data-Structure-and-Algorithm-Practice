from bisect import bisect_left

def binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False

list = ['apple','banana','orange','kiwi']
value = 'banana'
binary_search(an_iterable=list, target=value)