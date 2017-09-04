def print_combinations(l):
    for i in l:
        if isinstance(i, list):
            print_combinations(i)
        else:
            print i,
    print


result = []


def combinations(arr, r, headlist=[]):
    l = len(arr)
    if r <= 0:
        headlist.sort()
        if headlist not in result:
            result.append(headlist)
    else:
        appendlist = list(headlist)
        for i in range(l - r + 1):
            appendlist.append(arr[i])
            combinations(arr[i + 1:], r - 1, appendlist)
            appendlist = list(headlist)


A = [1, 2, 3]
r = 2

combinations(A, r)
print "Total Combinations = ", len(result)
print_combinations(result)
