# 选择排序
def select_sort(items, cmp = lambda x, y: x < y): 
    items = list(items)
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if cmp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

# 冒泡排序
def bubble_sort(items, cmp = lambda x, y: x > y):
    items = list(items)
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if cmp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

# 归并排序
def merge_sort(items, cmp = lambda x, y: x < y):
    items = list(items)
    return _merge_sort(items, cmp)

def _merge_sort(items, cmp):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], cmp)
    right = _merge_sort(items[mid:], cmp)
    return merge(left, right, cmp)

def merge(left, right, cmp):
    items = []
    left_index, right_index = 0, 0
    while(left_index < len(left) and right_index < len(right)):
        if(cmp(left[left_index], right[right_index])):
            items.append(left[left_index])
            left_index += 1
        else:
            items.append(right[right_index])
            right_index += 1
    items += left[left_index:]
    items += right[right_index:]
    return items

# 快速排序 Lomuto 分区方案
def quick_sort(items, cmp = lambda x, y: x <= y):
    items = list(items)
    _quick_sort(items, 0, len(items) - 1, cmp)
    return items

def _quick_sort(items, start, end, cmp):
    if start < end:
        pos = _partition(items, start, end, cmp)
        _quick_sort(items, start, pos -1, cmp)
        _quick_sort(items, pos + 1, end, cmp)

def _partition(items, start, end, cmp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if(cmp(items[j], pivot)):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1

